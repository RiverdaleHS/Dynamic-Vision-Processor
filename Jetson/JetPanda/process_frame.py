import cv2
import numpy as np



def process_frame(frame, low_range, high_range, focal_length, targets):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Hue 0-180
    # Saturation 0-255
    # Value 0-255

    binary = cv2.inRange(hsv, low_range, high_range)
    # clean up binary frame

    erode_binary = cv2.erode(binary, np.ones((4, 4), np.uint8), iterations=1)
    open_binary = cv2.dilate(erode_binary, np.ones((4, 4), np.uint8), iterations=4)

    _, contours, hierarchy = cv2.findContours(open_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for target in targets:
        contours.sort(key=target.sorter)
        for i in range(target.number_of_targets):
            target.add_contour(contours[i])
        xs = 0
        ys = 0
        for cnt in target.contours:
            M = cv2.moments(cnt)
            xs += int(M['m10']/M['m00'])
            ys += int(M['m01'] / M['m00'])
        x = xs / len(target.contours)
        y = ys / len(target.contours)
        target.set_point(x, y)

    return targets
