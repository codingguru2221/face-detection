# Webcam Image Capture Project

## Description
This project allows users to capture images from a webcam and store them in a designated folder. It utilizes the OpenCV library for video processing and face detection.

## Prerequisites
- Python 3.x
- OpenCV library

To install OpenCV, run the following command:

## How to Use
1. Make sure your webcam is connected and operational.
2. Execute the script:
   ```bash
   python try1.py
   ```
3. A window will appear showing the live feed from your webcam.
4. Use the following keys to interact with the program:
   - `ESC`: Close the program.
   - `SPACE`: Capture the current frame and save it as an image.
   - `q`: Close the program.

## Output
Captured images will be stored in the `dataset` folder, named in the format `user_{user_id}_{img_counter}.jpg`.

## License
This project is open-source and can be modified and shared freely.
