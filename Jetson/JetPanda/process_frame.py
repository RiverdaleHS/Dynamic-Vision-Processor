import cv2
import numpy as np


def process_frame(frame, low_range, high_range, target):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Hue 0-180
    # Saturation 0-255
    # Value 0-255

    binary = cv2.inRange(hsv, low_range, high_range)
    morph_binary = binary
    # clean up binary frame
    kernal = np.ones((16, 16), np.uint8)
    cv2.morphologyEx(morph_binary, cv2.MORPH_OPEN, kernal)


    #_, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (255, 140, 0), -1)
    cv2.imshow("frame", frame)
    cv2.imshow("binary", binary)
    cv2.imshow("morphed binary", morph_binary)
