import cv2

# Open the default webcam (use 0 for the default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    try:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # If frame is read correctly, ret is True
        if not ret:
            print("Error: Failed to grab frame.")
            break
        
        # Display the resulting frame
        frame = cv2.imread('frame.jpg')
        cv2.imshow('Webcam Feed', frame)
        
        # Press 'q' to exit the webcam feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        continue

# Release the capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

