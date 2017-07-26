import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
from util import *


# Input variables that will be command line args in a later release
ROBOT_FILE_PATH = "robot.panda"
CAMERA_FILE_PATH = "camera.panda"

# Global Variables are all stored in this dict
global_vars = {}

# Print Dependency Versions
print("Using OpenCV " + cv2.__version__)  # Print OpenCV Version



try:  # Load Robot File
    with open(ROBOT_FILE_PATH) as robot_file:
        read_from_file(robot_file, global_vars)

except:
    print("Could not find robot description file " + ROBOT_FILE_PATH)
    print("Creating file " + ROBOT_FILE_PATH)
    new_robot_file = open(ROBOT_FILE_PATH, "w+")
    robot_hostname = input("What is the hostname of the RoboRIO?")
    new_robot_file.write("RoboRIO_Hostname|" + robot_hostname + "\n")
    new_robot_file.close()
    with open(ROBOT_FILE_PATH) as robot_file:
        read_from_file(robot_file, global_vars)

print("Successfully loaded robot file " + ROBOT_FILE_PATH)

try:  # Load Camera File
    with open(CAMERA_FILE_PATH) as camera_file:
        read_from_file(camera_file, global_vars)

except:
    print("Could not find camera description file " + CAMERA_FILE_PATH)
    print("Creating file " + CAMERA_FILE_PATH)
    new_camera_file = open(CAMERA_FILE_PATH, "w+")
    # Camera USB Name
    cam_id = input("What is the USB ID of this Camera?")
    new_camera_file.write("Camera_ID|" + cam_id + "\n")
    # Focal Lenght
    focal_length = input("What is the focal length of this camera?")
    new_camera_file.write("Camera_Focal_Length|" + focal_length + "\n")
    # Heigth off of Ground
    ground_height = input("How far off the ground is this camera?")
    new_camera_file.write("Camera_Ground_Height|" + ground_height + "\n")
    # HSV
    min_hue = input("What is the minimum hue to threshold?")
    max_hue = input("What is the maximum hue to threshold?")
    min_saturation = input("What is the minimum saturation to threshold?")
    max_saturation = input("What is the maximum saturation to threshold?")
    min_value = input("What is the minimum value to threshold?")
    max_value = input("What is the maximum value to threshold?")
    ###
    new_camera_file.write("min_hue|" + min_hue + "\n")
    new_camera_file.write("max_hue|" + max_hue + "\n")
    new_camera_file.write("min_saturation|" + min_saturation + "\n")
    new_camera_file.write("max_saturation|" + max_saturation + "\n")
    new_camera_file.write("min_value|" + min_value + "\n")
    new_camera_file.write("max_value|" + max_value + "\n")
    #####
    new_camera_file.close()
    with open(CAMERA_FILE_PATH) as camera_file:
        read_from_file(camera_file, global_vars)

print("Successfully loaded camera file " + CAMERA_FILE_PATH)