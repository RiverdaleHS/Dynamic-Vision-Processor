import cv2

def process_frame(frame, low_range, high_range, target):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #binary = cv2.inRange(hsv, (10, 10, 10), (200, 200, 200))
    random_image_why_is_this_here, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, -1, (0, 255, 0), 3)
    cv2.imshow("raw", frame)
    #cv2.imshow("binary", binary)