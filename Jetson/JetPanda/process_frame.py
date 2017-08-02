import cv2
import numpy as np
import math

def process_frame(frame, low_range, high_range, targets):
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

    _, contours, hierarchy = cv2.findContours(open_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    filtered_contours = []
    # Find Targets
    for contour in contours:
        # Eliminate small contours based on a fit line.  All targets should be level to the ground
        [vx, vy, x, y] = cv2.fitLine(contour, cv2.DIST_L2, 0, 0, 0.01, 0.01)
        if math.degrees(math.atan2(vy - y, vx - x)) > 45:
            targets.append(contour)

    for filtered_contour in filtered_contours:
        for target in targets:
            area = cv2.contourArea(contour)
            perimeter = cv2.arcLength(contour, True)


    cv2.drawContours(frame, contours, -1, (255, 140, 0), -1)
    cv2.imshow("frame", frame)
    cv2.imshow("binary", binary)
    cv2.imshow("erode binary", erode_binary)
    cv2.imshow("open binary", open_binary)