import cv2
from target import *


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

# returns an array of target objects with all of the needed info
# def read_from_targets_file(file):
#     targets = []
#     lines = file.readlines()
#     for line in lines:
#         data = line.split("|")
#         file_path = data[0]
#         function_name = data[1]
#         number_of_targets_wanted = data[2]
#
#         targets.append(target())
#     return target_file_paths


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
