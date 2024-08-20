import cv2
import requests
import pickle
import time

# Open the webcam
cap = cv2.VideoCapture(0)  # 0 is typically the default webcam

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Display the frame
    #cv2.imshow('Webcam Feed', frame)

    cv2.imwrite("frame.jpg", frame)

    requests.post("http://127.0.0.1", files={"file": open("frame.jpg", "rb")})

    time.sleep(5)


# Release the webcam and close windows
cap.release()

