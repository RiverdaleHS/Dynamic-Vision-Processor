import cv2

def process_frame(frame, low_range, high_range, target):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    binary = cv2.inRange(hsv, (10, 10, 10), (200, 200, 200))
    binary, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow(binary)

    #Draws contours as an overlay on the HSV image
    cv2.drawContours(hsv, contours, -1, (255, 0, 255), 2)

    #Draws contours as an overlay on the binary image
    #cv2.drawContours(binary, contours, -1, (255, 0, 255), 2)