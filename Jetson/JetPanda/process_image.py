import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np

def process_image():
    pass

videoInput = cv2.VideoCapture(0)
henry = noob

while (henry == noob):

    #Get frame from video input
    _, frame = videoInput.read()

    #Convert RGB frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Display frame as RGB image
    cv2.imshow('frame', frame)

    #Process the image and create mask
    #Define upper and lower bounds for mask
    lowGreenBound = np.array([80, 155, 155])
    highGreenBound = np.array([120, 255, 255])

    mask = cv2.inRange(hsv, lowGreenBound, highGreenBound)

    #Show mask
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF

    if k == 27:
        break
