# 👀 Real-Time Face Detection with OpenCV 🎥

This project demonstrates real-time face detection using OpenCV's Haar Cascade Classifier. The program captures video from your webcam, detects faces in real-time, and highlights them with bounding boxes.

---

## 🛠 Features
- **Real-Time Face Detection**: Utilizes Haar cascades to identify faces in video frames.
- **Customizable Detection**: Adjustable parameters like scale factor, minimum neighbors, and face size for optimized detection.
- **Webcam Integration**: Captures video directly from your webcam for live face tracking.

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.8 or higher**
- **OpenCV**: Install it using:
  ```bash
  pip install opencv-python
Setup
1. Clone this repository:
    ```bash
    git clone https://github.com/nofilsiddiqui-2000/Practice-Projects.git
    cd "Practice-Projects/face-detection"

2. Ensure the Haar cascade file haarcascade_frontalface_default.xml is in the same directory as the script. If not, download it from OpenCV GitHub.

🖥️ How to Run
1. Open your terminal and navigate to the project directory:
    ```bash
    cd "Practice-Projects/face-detection"

2. Run the script:
    ```bash
    python face_detection.py

🔧 How It Works
1. Initialize Haar Cascade: Load the pre-trained Haar cascade XML file for face detection.
2. Video Capture: Use OpenCV to access the webcam feed.
3. Face Detection: Convert video frames to grayscale and apply the Haar cascade to detect faces.
4. Bounding Boxes: Draw rectangles around detected faces in real-time.
5. Display Feed: Render the video feed with highlighted faces.

🛠 Future Improvements
- Add face tracking for smoother detection.
- Integrate additional Haar cascades for detecting other objects (e.g., eyes, smiles).
- Save detected faces as image files for further processing.
- Implement support for processing static images or video files.

⚠️ Note
- The Haar cascade algorithm is efficient but may not work well in all lighting conditions or with occluded faces. For higher accuracy, consider using modern deep learning-based detectors like DNNs or CNNs.

✨ Credits
- OpenCV Documentation
- Haar cascades are part of the OpenCV library.


