import cv2
import os

def capture_images(user_id):
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not open camera.")
        return

    cv2.namedWindow("Capture Images")
    img_counter = 0

    # Ensure the dataset directory exists
    os.makedirs("dataset", exist_ok=True)

    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("Capture Images", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:  # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:  # SPACE pressed
            img_name = f"user_{user_id}_{img_counter}.jpg"
            cv2.imwrite(os.path.join("dataset", img_name), frame)
            print(f"{img_name} written!")
            img_counter += 1
        elif k % 256 == ord('q'):  # 'q' pressed
            print("Q hit, closing...")
            break

    cam.release()
    cv2.destroyAllWindows()
    print("Program closed successfully.")

# Example usage
capture_images(1)
