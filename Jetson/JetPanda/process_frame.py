import cv2
import numpy as np


def process_frame(frame, low_range, high_range, target):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Hue 0-180
    # Saturation 0-255
    # Value 0-255

    binary = cv2.inRange(hsv, low_range, high_range)
    # clean up binary frame
    erode_kernal = np.ones((4, 4), np.uint8)
    dilate_kernal = np.ones((4, 4), np.uint8)
    erode_binary = cv2.erode(binary, erode_kernal, iterations=1)
    open_binary = cv2.dilate(binary, dilate_kernal, iterations=1)

    #_, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (255, 140, 0), -1)
    cv2.imshow("frame", frame)
    cv2.imshow("binary", binary)
    cv2.imshow("erode binary", erode_binary)
    cv2.imshow("open binary", open_binary)
