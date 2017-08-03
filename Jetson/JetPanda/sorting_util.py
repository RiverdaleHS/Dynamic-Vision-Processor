import cv2

def target_area(target):
    return cv2.contourArea(target)

def target_perimeter(target):
    return cv2.arcLength(target)