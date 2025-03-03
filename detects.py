import argparse
from ultralytics import YOLO
import cv2
import pandas as pd
from datetime import datetime
import os
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser(description="YOLOv8 Surveillance and Classroom Monitoring System")
    parser.add_argument('--weights', type=str, default='yolov8n.pt', help='Path to weights file')
    parser.add_argument('--source', type=str, default='http://192.168.42.137:4747/video', help='Source for detection (DroidCam URL or path for images/videos)')
    parser.add_argument('--img-size', type=int, default=640, help='Image size for inference')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='Confidence threshold for detection')
    parser.add_argument('--mode', type=str, default='classroom', choices=['classroom'], help='Mode of operation')
    parser.add_argument('--save', action='store_true', help='Save inference results')
    return parser.parse_args()

CSV_FILE = "classroom_attendance.csv"

if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=['Name', 'Entry Time', 'Exit Time'])
    df.to_csv(CSV_FILE, index=False)

def is_person_in_class(name):
    df = pd.read_csv(CSV_FILE)
    if name in df['Name'].values and pd.isna(df[df['Name'] == name]['Exit Time'].values[0]):
        return True
    return False

def log_entry(name):
    df = pd.read_csv(CSV_FILE)
    if name not in df['Name'].values:
        new_row = {'Name': name, 'Entry Time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Exit Time': None}
        df = df.append(new_row, ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

def log_exit(name):
    df = pd.read_csv(CSV_FILE)
    if name in df['Name'].values and pd.isna(df[df['Name'] == name]['Exit Time'].values[0]):
        df.loc[df['Name'] == name, 'Exit Time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df.to_csv(CSV_FILE, index=False)

# Function for classroom monitoring
def monitor_classroom(results, unique_ids):
    total_count = 0
    for result in results:
        name = result.names[0]
        unique_id = result.id  # Assuming the model provides a unique ID for each detected object

        if unique_id not in unique_ids:
            unique_ids.add(unique_id)
            total_count += 1
            
            if "student" in name.lower():
                log_entry(name)
            elif "teacher" in name.lower():
                print(f"Teacher detected: {name} (highlighting in a different color)")
                log_entry(name)

    return total_count

# Function to run YOLO detection
def run_detection(weights, source, img_size, conf_thres, mode, save):
    model = YOLO(weights)
    unique_ids = set()  # Set to keep track of unique IDs
    total_count = 0

    cap = cv2.VideoCapture(source)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(source=frame, imgsz=img_size, conf=conf_thres, show=False)
        
        if mode == 'classroom':
            total_count = monitor_classroom(results, unique_ids)

        # Display total count on the frame
        cv2.putText(frame, f'Total Count: {total_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('YOLOv8 Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    args = parse_args()
    run_detection(args.weights, args.source, args.img_size, args.conf_thres, args.mode, args.save)