import cv2
from target import *
import math

# loads config file
def read_from_file(file, output_dict):
    lines = file.readlines()
    for line in lines:
        data = line.split("|")
        name_of_constant = data[0]
        constant = data[1]
        if isInt(constant):
            output_dict[name_of_constant] = int(constant)
        else:
            output_dict[name_of_constant] = constant

def isInt(string):
    try:
        int(string)
        return True
    except:
        return False


def createTrackbar(window, name, min, max):
    cv2.createTrackbar(name, window, min, max, trackbarValueDidChange)


def trackbarValueDidChange(x):
    pass


def readTrackbar(window, name):
    pass



def getHorizontalAngle(x, image_width, focal_length):
    image_width_center = (image_width - 1)/2
    radians_yaw = math.atan((x - image_width_center )/ focal_length)
    degrees_yaw = math.degrees(radians_yaw)
    return degrees_yaw

def getVerticalAngle(y, image_height, focal_length):
    image_height_center = (image_height - 1)/2
    radians_pitch = math.atan((y - image_height_center )/ focal_length)
    degrees_pitch = math.degrees(radians_pitch)
    return degrees_pitch

def getDistanceToTarget(target_height, camera_height, degrees_pitch): #Camera pitch is assumed to be 90°
    height_differential = math.fabs(target_height - camera_height)
    distance_to_target = height_differential * math.tan(degrees_pitch)

    return distance_to_target

def createHSVThreasholdTrackbars(output_dict):
    cv2.namedWindow("HSV_Range")
    createTrackbar("HSV_Range", "min_hue", 0, 180)
    createTrackbar("HSV_Range", "max_hue", 0, 180)
    createTrackbar("HSV_Range", "min_saturation", 0, 255)
    createTrackbar("HSV_Range", "max_saturation", 0, 255)
    createTrackbar("HSV_Range", "min_value", 0, 255)
    createTrackbar("HSV_Range", "max_value", 0, 255)
    setTrackbarPosition("HSV_Range", "h_min", output_dict["min_hue"])
    setTrackbarPosition("HSV_Range", "h_min", output_dict["max_hue"])
    setTrackbarPosition("HSV_Range", "h_min", output_dict["min_saturation"])
    setTrackbarPosition("HSV_Range", "h_min", output_dict["max_saturation"])
    setTrackbarPosition("HSV_Range", "h_min", output_dict["min_value"])
    setTrackbarPosition("HSV_Range", "h_min", output_dict["max_value"])

def setTrackbarPosition(window, name, position):
    cv2.setTrackbarPos(window, name, position)

degrees_yaw = (getHorizontalAngle(45, 640, 554.3))
degrees_pitch = (getVerticalAngle(250, 480, 554.3))
