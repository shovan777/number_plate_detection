"""Capture images from video."""
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # print(gray.shape)

    # Draw bounding bbox
    cv2.rectangle(gray, (280, 100), (440, 400), (0, 255, 0), 2)

    # display text
    cv2.putText(gray, "person", (280, 80), 0, 0.3, (0, 0, 255))

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
