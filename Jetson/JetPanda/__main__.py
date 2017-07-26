import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2

# Input variables that will be command line args in a later release
ROBOT_FILE_PATH = "robot.panda"

# Global Variables are all storsed in this dict
global_vars = {}

# Print Dependency Versions
print("Using OpenCV " + cv2.__version__)  # Print OpenCV Version

# Load Description Files
try:
    with open(ROBOT_FILE_PATH) as robot_file:
        hostname_line = robot_file.read()
        robot_hostname = hostname_line.split("|")[1]
        global_vars["RoboRio_Hostname"] = robot_hostname


except:
    print("Could not find robot description file " + ROBOT_FILE_PATH)
    print("Creating file " + ROBOT_FILE_PATH)
    new_robot_file = open(ROBOT_FILE_PATH, "w+")
    robot_hostname = input("What is the hostname of the RoboRIO")
    new_robot_file.write("RoboRIO_Hostname|" + robot_hostname)
    new_robot_file.close()
    global_vars["RoboRio_Hostname"] = robot_hostname

print("Successfully loaded robot file " + ROBOT_FILE_PATH + ", with hostname " + global_vars["RoboRio_Hostname"])

#Load test images for later use
testImage1 = cv2.imread('testImage-1.jpg',cv2.IMREAD_COLOR)
testImage2 = cv2.imread('testImage-2.jpg',cv2.IMREAD_COLOR)
testImage3 = cv2.imread('testImage-4.jpg',cv2.IMREAD_COLOR)
testImage4 = cv2.imread('testImage-5.jpg',cv2.IMREAD_COLOR)
testImage5 = cv2.imread('testImage-8.jpg',cv2.IMREAD_COLOR)