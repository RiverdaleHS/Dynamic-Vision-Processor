import cv2


def process_frame(frame, low_range, high_range, target):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Hue 0-180
    # Saturation 0-255
    # Value 0-255

    binary = cv2.inRange(hsv, low_range, high_range)
    # random_image_why_is_this_here, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame, -1, (0, 255, 0), 3) THIS IS CAUSING PROBLEMS
    cv2.imshow("raw", frame)
    cv2.imshow("binary", binary)
