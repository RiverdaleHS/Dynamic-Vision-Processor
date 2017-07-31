import cv2

def process_frame(frame, vars):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    binary = cv2.inRange(hsv, (10, 10, 10), (200, 200, 200))
    cv2.imshow(binary)