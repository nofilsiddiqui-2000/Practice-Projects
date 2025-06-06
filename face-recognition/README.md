# Face Recognition with PyTorch

This project demonstrates a simple face recognition system using the [facenet-pytorch](https://github.com/timesler/facenet-pytorch) library. It matches unknown faces against a folder of known individuals and reports the closest match.

## Features
- Uses a pre-trained FaceNet model for generating face embeddings.
- Automatically detects and aligns faces with MTCNN.
- Compares embeddings with Euclidean distance to recognize faces.

## Requirements
- Python 3.8+
- torch
- facenet-pytorch
- numpy
- opencv-python

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage
1. Place reference images in a directory structure like:
   ```
   known_faces/
       alice/
           img1.jpg
           img2.jpg
       bob/
           pic.jpg
   ```
2. Run the recognition script on a target image:
   ```bash
   python recognize.py --known_dir known_faces --image path/to/test.jpg
   ```
3. The script prints the name of the closest match or `Unknown` if no match passes the threshold.

## Notes
- The model is pre-trained on VGGFace2 and works best with clear frontal faces.
- Adjust the `--threshold` argument to tune recognition strictness.
