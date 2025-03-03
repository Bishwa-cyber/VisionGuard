import argparse
from ultralytics import YOLO
import cv2
import pandas as pd
from datetime import datetime
import os

def parse_args():
    parser = argparse.ArgumentParser(description="YOLOv8 Surveillance and Classroom Monitoring System")
    parser.add_argument('--weights', type=str, default='yolov8n.pt', help='Path to weights file')
    parser.add_argument('--source', type=str, default='0', help='Source for detection (0 for webcam, path for images/videos)')
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

# Function to log entry time of a student or teacher
def log_entry(name):
    df = pd.read_csv(CSV_FILE)
    if name not in df['Name'].values:
        new_row = {'Name': name, 'Entry Time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Exit Time': None}
        df = df.append(new_row, ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

# Function to log exit time of a student or teacher
def log_exit(name):
    df = pd.read_csv(CSV_FILE)
    if name in df['Name'].values and pd.isna(df[df['Name'] == name]['Exit Time'].values[0]):
        df.loc[df['Name'] == name, 'Exit Time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df.to_csv(CSV_FILE, index=False)

# Function for classroom monitoring
def monitor_classroom(results):
    # Iterate over detection results
    for result in results:
        name = result.names[0] 
        
       
        if "student" in name.lower():
            if not is_person_in_class(name):
                log_entry(name)
            else:
                log_exit(name)
        
       
        elif "teacher" in name.lower():
            print(f"Teacher detected: {name} (highlighting in a different color)")
            if not is_person_in_class(name):
                log_entry(name)
          
        
        print(f"Classroom monitoring result: {name}")
def run_detection(weights, source, img_size, conf_thres, mode, save):
    model = YOLO(weights)
    if source == '0':
        source = 0 
    results = model.predict(source=source, imgsz=img_size, conf=conf_thres, show=True)
    if mode == 'classroom':
        monitor_classroom(results)
    if save:
        results.save()
if __name__ == '__main__':
    args = parse_args()
    run_detection(args.weights, args.source, args.img_size, args.conf_thres, args.mode, args.save)
