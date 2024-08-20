import cv2
import requests
import pickle

# Open the webcam
cap = cv2.VideoCapture(0)  # 0 is typically the default webcam

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Display the frame
    #cv2.imshow('Webcam Feed', frame)

    serialized = pickle.dumps(frame)
    requests.post("127.0.0.1", data={"data": serialized})


# Release the webcam and close windows
cap.release()

