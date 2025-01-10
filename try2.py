import cv2
import os
from deepface import DeepFace

def authenticate_user():
    known_image_path = "ref.jpg"
    known_image = cv2.imread(known_image_path)

    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not open camera.")
        return False

    cv2.namedWindow("Authenticate User")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        try:
            result = DeepFace.verify(frame, known_image, model_name='VGG-Face', enforce_detection=False)
            if result["verified"]:
                print("Authentication successful!")
                cam.release()
                cv2.destroyAllWindows()
                return True
        except ValueError as e:
            print(f"Error during verification: {e}")

        cv2.imshow("Authenticate User", frame)

        k = cv2.waitKey(1)
        if k % 256 == ord('q'):  # 'q' pressed
            print("Q hit, closing...")
            break

    cam.release()
    cv2.destroyAllWindows()
    print("Authentication failed!")
    return False

def capture_images(user_id):
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not open camera.")
        return

    cv2.namedWindow("Capture Images")
    img_counter = 0

    # Ensure the dataset directory exists
    os.makedirs("dataset", exist_ok=True)

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

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

# Main function to run the program
if authenticate_user():
    capture_images(1)
