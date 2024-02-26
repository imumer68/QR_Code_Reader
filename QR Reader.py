import cv2
import numpy as np
from pyzbar.pyzbar import decode


def scan_codes(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Decode barcodes and QR codes from the grayscale frame
    decoded_objects = decode(gray)

    # Loop through the detected objects
    for obj in decoded_objects:
        # Extract the barcode or QR code data
        data = obj.data.decode("utf-8")

        # Extract the bounding box coordinates
        points = obj.polygon

        # Convert the list of points into a numpy array
        points = np.array(points, dtype=np.int32)

        # Draw the bounding box around the detected object
        cv2.polylines(frame, [points], True, (0, 255, 0), 2)

        # Print the type and data of the detected object
        print(f"Type: {obj.type}, Data: {data}")


def main():
    # Open the default camera (usually the first camera found)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    # Loop to continuously capture frames from the camera
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break

        # Flip the frame horizontally for a mirror effect
        frame = cv2.flip(frame, 1)

        # Scan and decode barcodes and QR codes in the frame
        scan_codes(frame)

        # Display the frame
        cv2.imshow('Barcode and QR Code Scanner', frame)

        # Check for the 'q' key to quit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
