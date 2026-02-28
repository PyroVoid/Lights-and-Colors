from typing import Any

import cv2
import numpy as np
from numpy import dtype, ndarray




def webcamPhoto(cap: cv2.VideoCapture)-> ndarray[tuple[Any, ...], dtype[Any]] | None | Any:
    worked, photo_array = cap.read()
    cv2.imshow("Photo", photo_array)
    if worked:
        return photo_array
    else:
        print("Webcam not working")
        return None


def test():
    cap = cv2.VideoCapture(0)

    # Check if the camera opened
    if not cap.isOpened():
        print("Camera failed to open.")
    else:
        # Read one frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame.")
        else:
            photo = frame
            print("Photo captured")
            return photo


def algorithm():
    frame1 = test()
    frame2 = test()
    difference = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY, difference)
    _, threshold = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros_like(gray)
    cv2.drawContours(mask, contours, -1, 255, -1)




test()