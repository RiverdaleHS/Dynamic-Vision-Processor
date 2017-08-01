import cv2
import numpy as np


def process_frame(frame, low_range, high_range, target):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Hue 0-180
    # Saturation 0-255
    # Value 0-255

    binary = cv2.inRange(hsv, low_range, high_range)
    #dialate image
    kernal = np.ones((5,5), np.uint8)
    cv2.dilate(binary, kernal, iterations=1)


    #_, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (255, 140, 0), -1)
    cv2.imshow("frame", frame)
    cv2.imshow("binary", binary)
