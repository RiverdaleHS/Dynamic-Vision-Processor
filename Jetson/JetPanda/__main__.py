import numpy as np
import cv2
<<<<<<< HEAD
import sys, inspect
=======
import sys
import math
>>>>>>> dc94f999bed99ebf16cd392e81a52fba602dda38
from util import *
from process_frame import *
from target import *
global_vars = {}
from demo_target_sorter import demo_target_fitness

# attempt to load commandline args and if they are not there correct the user
try:
    config_file_path = sys.argv[1]
    target_file_path = sys.argv[2]
    #remove .py extension if
    target_file_name = target_file_path.split(".")[0]
    target_functions_file = __import__(target_file_name)
    all_fucntions_in_target_file = [f for f in inspect.getmembers(target_functions_file) if inspect.isfunction(f[1])]\

    for function in all_fucntions_in_target_file:
        print(__name__(function))
        # for memeber in inspect.getmembers(function):
        #     print(memeber)

    # for func in all_fucntions_in_target_file:
    #     print(inspect.getargvalues(func))

    print(all_fucntions_in_target_file)

    image_source = sys.argv[3]
except Exception as e:
    print("Usage: python3 __main__.py config_file_path camera_id_or_image_path")
    print(e)
    exit(-0)

try:  # Load Config File
    with open(config_file_path) as config_file:
        read_from_file(config_file, global_vars)
except:
    print("Could not find config file " + config_file_path)
    print("Creating file " + config_file_path)
    config_file = open(config_file_path, "w+")
    #Define variables necessary for angle calculation
    imageWidth, imageHeight = cv.GetSize(src)
    centerX = imageWidth / 2 - 0.5
    centerY = imageHeight / 2 - 0.5
    #Robot Hostname
    robot_hostname = input("What is the hostname of the RoboRIO?")
    config_file.write("RoboRIO_Hostname|" + robot_hostname + "\n")
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
                          [target(demo_target_fitness, 1)])  # PLACE HOLDERS
        except Exception as e:
            print("Main Loop Failure!!!🤔")
            print(e)
        if cv2.waitKey(1) == 27:
            camera.release()
            break
else:
    # Load one image and display in loop
    print("Loading Image " + image_source)
    while True:
        try:

            raw_frame = cv2.imread(image_source)

            process_frame(raw_frame, (global_vars["min_hue"], global_vars["min_saturation"], global_vars["min_value"]),
                          (global_vars["max_hue"], global_vars["max_saturation"], global_vars["max_value"]),
                          [target(demo_target_fitness, 1)])  # PLACE HOLDERS


        except Exception as e:
            print("Failed to Load Image!!!🤔")
            print(e)
            break
        if cv2.waitKey(1) == 27:
            break
cv2.destroyAllWindows()