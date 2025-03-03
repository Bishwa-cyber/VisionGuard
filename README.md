# **VisionGuard: Real-Time Object Detection and Monitoring System**  
**VisionGuard** is an advanced real-time object detection and monitoring system, designed to track, analyze, and process video streams from IP cameras or video sources. This system is ideal for environments such as classrooms, warehouses, factories, and surveillance areas. It uses YOLOv8 to detect various objects like people, machinery, and equipment, providing dynamic people counting, object tracking, and safety monitoring features.

---

## **Features**
- **Real-Time Object Detection:** Detects objects such as people, chairs, laptops, machinery, and other items in live video streams.
- **Multiple Input Sources:** Supports IP cameras, webcam feeds, and local video files.
- **Dynamic People Counting:** Logs entry/exit of people detected in the stream and tracks the current number of people.
- **Customizable Object Detection:** Detects various objects (e.g., vehicles, equipment, furniture) with the ability to customize the types of objects to detect.
- **CSV Logging:** Attendance and object detection logs are stored in `.csv` files for future analysis.
- **Web Integration:** Displays raw and processed video streams (with detection overlays) on a web interface.
- **Real-Time Alerts:** Alerts for flagged objects (e.g., worker without safety equipment) in real-time.



## **Requirements**
Ensure you have the following dependencies installed before running the project:


**pip install opencv-python
pip install ultralytics
pip install ffmpeg-python
pip install pandas
**

Additional Requirements:

Node.js for the web interface.
FFmpeg (for handling video streams).
Steps to Run the Project
1. Clone the Repository:
Download the project to your system.

bash
Copy
Edit
git clone https://github.com/yourusername/VisionGuard.git
cd VisionGuard
2. Install Python Dependencies:
bash
Copy
Edit
pip install -r requirements.txt
3. Install Node.js Dependencies (for the web interface):
Navigate to the frontend directory and install the required Node.js packages:

bash
Copy
Edit
cd frontend
npm install
4. Start Object Detection:
Run the detection system with the following command:

bash
Copy
Edit
python detects.py --weights yolov8n.pt --source "http://192.168.42.137:4747/video" --conf-thres 0.25 --img-size 640 --mode monitor
weights: YOLOv8 model weights (e.g., yolov8n.pt).
source: Video source (e.g., IP camera stream or video file).
conf-thres: Confidence threshold for detection.
img-size: Image size for inference.
mode: Set to monitor for real-time monitoring.
5. Run the Web Interface:
bash
Copy
Edit
npm start
Access the web interface at http://localhost:3000/dashboard.

### Project Workflow



1. Video Stream and Object Detection
The system captures the live video stream (IP camera or video file) and runs the object detection using YOLOv8.
Object detections are drawn as bounding boxes over the live video.
2. Log People and Object Data
The system logs the detection of people, machinery, and other objects in real-time.
CSV files store the detection data, including timestamps for people entering/exiting the monitored area.
3. Display Raw and Processed Video
Raw video (without detections) and processed video (with object detections) are displayed side-by-side on the web interface.



Flowchart

flowchart TD
    A[Start] --> B[Capture Video Feed]
    B --> C[Send Feed to Python Backend]
    C --> D[Run YOLOv8 Detection on Each Frame]
    D --> E[Draw Bounding Boxes, Log Detected Objects]
    E --> F[Stream Processed Frames via Flask]
    F --> G[Serve Frames to Web Interface]
    G --> H[Display Raw & Processed Streams on Dashboard]
    H --> I[Logs Saved to CSV for Analysis]
    I --> J[End]

### Project Structure


VisionGuard/
│
├── detects.py                # Main script for real-time detection
├── requirements.txt          # Python dependencies
├── frontend/                 # Web interface (Express.js)
│   ├── views/                # EJS templates
│   ├── public/               # Static files (CSS, JS, images)
│   └── app.js                # Express.js server
├── static/                   # Static files for web interface
├── templates/                # EJS templates for web pages
├── flask_server.py           # Flask server to stream processed video
└── README.md                 # Project documentation


Demo
### Watch a demo of VisionGuard here.

**Real-Time Detection: Detect and track objects like people, chairs, and machinery.
Web Dashboard: Monitor the raw and processed video streams in real-time.
CSV Logging: Log object detections for further analysis.
Contributors
Bishwa Bhushan Palar
Feel free to contribute by following the steps below:**

Fork the repository.
Create a new feature branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
If you have any questions or suggestions, feel free to reach out to bishwapalar657@gmail.com.

