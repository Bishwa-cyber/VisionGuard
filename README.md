# VisionGuard

**VisionGuard** is an advanced real-time object detection and monitoring system built using YOLOv8. It can detect, track, and log various objects, including people, machinery, and equipment, from live video streams such as IP cameras or local video files. It is designed for environments like classrooms, factories, and warehouses, providing dynamic object tracking and people counting features for enhanced monitoring and safety.

![VisionGuard Banner](https://yourimageurl.com/banner-image) <!-- Optional banner image -->

## Features
- **Real-Time Object Detection**: Tracks objects such as people, machinery, and furniture in live video streams using YOLOv8.
- **Multiple Input Sources**: Supports IP cameras, webcam, and pre-recorded video files.
- **Dynamic People Counting**: Automatically logs entry/exit times and provides a live count of people detected in the video.
- **Custom Object Detection**: Easily customizable for detecting any objects of interest.
- **CSV Logging**: Logs detections with timestamps for future analysis.
- **Web Interface Integration**: View raw and processed video streams (object detection overlays) in a seamless web interface.
- **Support for Multiple Environments**: Ideal for classrooms, warehouses, factories, and security monitoring systems.

---

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Flowchart](#flowchart)
- [Project Structure](#project-structure)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

### Requirements
- **Python 3.8+**
- **Node.js** (for web interface)
- **ffmpeg** (for video stream handling)
- **pip** (for installing Python dependencies)

### Step 1: Clone the Repository

### git clone https://github.com/yourusername/VisionGuard.git
cd VisionGuard
Step 2: Install Python Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Step 3: Install Node.js Dependencies (For Web Interface)
Navigate to the frontend directory and install Node dependencies:

bash
Copy
Edit
cd frontend
npm install
Step 4: Install FFmpeg (Optional, for live stream handling)
Windows: FFmpeg Windows Installation Guide
Linux: Install via package manager:
bash
Copy
Edit
sudo apt install ffmpeg
macOS: Install via Homebrew:
bash
Copy
Edit
brew install ffmpeg
Usage
1. Start Object Detection (Python Backend)
To start object detection with a video source (e.g., an IP camera or local video file), run the following command:

bash
Copy
Edit
python detects.py --weights yolov8n.pt --source "http://192.168.42.137:4747/video" --conf-thres 0.25 --img-size 640 --mode monitor
weights: Path to the YOLOv8 model (e.g., yolov8n.pt).
source: IP camera stream or local video file.
conf-thres: Confidence threshold for detection.
img-size: Image size for inference.
mode: Set to monitor for real-time monitoring.
2. Start the Web Interface (Express.js Frontend)
To start the web interface that displays both raw and processed video streams, navigate to the frontend folder and run:

bash
Copy
Edit
npm start
Access the dashboard at http://localhost:3000/dashboard.

3. Live Stream Both Raw and Processed Videos
View the Raw Video Stream and Processed Object Detection Stream side by side on the web interface.
The processed stream will display bounding boxes for detected objects, people, etc.
Flowchart
Below is a flowchart to describe the VisionGuard process:


flowchart TD
    A[Start] --> B[Camera/Video Feed]
    B --> C[Send feed to Python Backend (OpenCV)]
    C --> D[Run YOLOv8 Detection on Each Frame]
    D --> E[Draw Bounding Boxes, Log Detected Objects]
    E --> F[Stream Processed Frames via Flask]
    F --> G[Serve Frames to Web Interface (Express.js)]
    G --> H[Display Raw & Processed Streams on Dashboard]
    H --> I[Logs Saved to CSV for Analysis]
    I --> J[End]

    
### Project Structure ###

VisionGuard/
│
├── detects.py                # Main Python script for object detection
├── requirements.txt          # Python dependencies
├── frontend/                 # Web interface (Express.js)
│   ├── views/
│   ├── public/
│   └── app.js                # Express.js server
├── static/                   # Static files (CSS, JS, images)
├── templates/                # EJS templates for web pages
├── flask_server.py           # Flask app to stream processed video
└── README.md                 # Project documentation


### Demo
You can watch a demo of VisionGuard here.

Real-time Detection: Detect people, objects, and count them dynamically.
Web Dashboard: Monitor both raw and processed streams via the web interface.
CSV Logging: Analyze object detection logs with timestamps.
Contributing
We welcome contributions! Here's how you can help:

 ### Fork the repository.
Create a new feature branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add a new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
### License
This project is licensed under the MIT License. See the LICENSE file for more details.
