import numpy as np
import cv2
import sys
from util import *
from process_frame import *

global_vars = {}

# attempt to load commandline args and if they are not there correct the user
try:
    config_file_path = sys.argv[1]
    image_source = sys.argv[2]
except:
    print("Usage: python3 __main__.py config_file_path camera_id_or_image_path")
    exit(-0)

try:  # Load Config File
    with open(config_file_path) as config_file:
        read_from_file(config_file, global_vars)
except:
    print("Could not find config file " + config_file_path)
    print("Creating file " + config_file_path)
    config_file = open(config_file_path, "w+")
    robot_hostname = input("What is the hostname of the RoboRIO?")
    config_file.write("RoboRIO_Hostname|" + robot_hostname + "\n")
    # Camera USB Name
    cam_id = input("What is the USB ID of this Camera?")
    config_file.write("Camera_ID|" + cam_id + "\n")
    # Focal Lenght
    focal_length = input("What is the focal length of this camera?")
    config_file.write("Camera_Focal_Length|" + focal_length + "\n")
    # Height off of Ground
    ground_height = input("How far off the ground is this camera?")
    config_file.write("Camera_Ground_Height|" + ground_height + "\n")
    # HSV
    min_hue = input("What is the minimum hue to threshold?")
    max_hue = input("What is the maximum hue to threshold?")
    min_saturation = input("What is the minimum saturation to threshold?")
    max_saturation = input("What is the maximum saturation to threshold?")
    min_value = input("What is the minimum value to threshold?")
    max_value = input("What is the maximum value to threshold?")

    config_file.write("min_hue|" + min_hue + "\n")
    config_file.write("max_hue|" + max_hue + "\n")
    config_file.write("min_saturation|" + min_saturation + "\n")
    config_file.write("max_saturation|" + max_saturation + "\n")
    config_file.write("min_value|" + min_value + "\n")
    config_file.write("max_value|" + max_value + "\n")

    config_file.close()
    with open(config_file_path) as robot_file:
        read_from_file(robot_file, global_vars)

print("Successfully loaded config file " + config_file_path)

# Print Dependency Versions
print("Using OpenCV " + cv2.__version__)  # Print OpenCV Version


if isInt(image_source):
    image_source = int(image_source)
    # Camera Loop!
    print("Loading Camera " + str(image_source))
    camera = cv2.VideoCapture(image_source)
    while True:
        try:
            ret, raw_frame = camera.read()
            process_frame(raw_frame, (global_vars["min_hue"], global_vars["min_saturation"], global_vars["min_value"]),
                          (global_vars["max_hue"], global_vars["max_saturation"], global_vars["max_value"]),
                          "Target")  # PLACE HOLDERS
        except Exception as e:
            print("Main Loop Failure!!!🤔")
            print(e)
        if cv2.waitKey(1) == 27:
            camera.release()
            break
else:
    # Load one image and display in loop
    print("Loading Image " + sys.argv[2])
    while True:
        try:

            raw_frame = cv2.imread(sys.argv[2])
            process_frame(raw_frame, (global_vars["min_hue"], global_vars["min_saturation"], global_vars["min_value"]),
                          (global_vars["max_hue"], global_vars["max_saturation"], global_vars["max_value"]),
                          "Target")  # PLACE HOLDERS


        except Exception as e:
            print("Failed to Load Image!!!🤔")
            print(e)
            break
        if cv2.waitKey(1) == 27:
            break
cv2.destroyAllWindows()
