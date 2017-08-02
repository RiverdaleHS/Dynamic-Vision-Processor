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
    # Remove crappy targets
    for contour in contours:
        # Eliminate small contours based on a fit line.  All targets should be level to the ground
        [vx, vy, x, y] = cv2.fitLine(contour, cv2.DIST_L2, 0, 0, 0.01, 0.01)
        area = math.degrees(math.atan2(vy - y, vx - x))
        if math.degrees(math.atan2(vy - y, vx - x)) < -150:
            filtered_contours.append(contour)


    for filtered_contour in filtered_contours:
        for target in targets:
            matches = []
            perimeter = cv2.arcLength(contour, True)
            area = cv2.contourArea(contour)
            perimeter_over_area = perimeter/area
            # 0.55 - 0.5 = 0.05
            if (perimeter_over_area - target.perimeter_over_area) < target.perimeter_over_area_tolerence:
                matches.append(target)

            if target.find_one:
                # determine the best of the found targets
                target.add_contours([matches[0]])
            else:
                target.add_contours(matches)



    cv2.drawContours(frame, contours, -1, (0, 0, 255), -1)
    cv2.drawContours(frame, filtered_contours, -1, (255, 0, 0), -1)
    for target in target:
        cv2.drawContours(frame, target.contours, -1, (0, 0, 255), -1)


    cv2.imshow("frame", frame)
    cv2.imshow("binary", binary)
    cv2.imshow("erode binary", erode_binary)