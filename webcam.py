import cv2

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()     # ret=True/False, frame = image

    if not ret:
        print("Could not read frame")
        break

    # Display the frame
    cv2.imshow("Webcam Feed", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting....")
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
