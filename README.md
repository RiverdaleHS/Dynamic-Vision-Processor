![Team 2915's Vision Processor](/text.gif?raw=true)

This program detects targets like these ones...

![Targets](/Jetson/JetPanda/testImages/testImage-2.png?raw=true)

Makes them look more like this using an HSV to binary filter

![Targets 2](/demoImage-1.png?raw=true)

Then, we identify the targets that meet the specifications set in the configuration file.

![Targets 3](/demoImage-2.png?raw=true)

This is how the robot sees the targets:

![Targets 4](/demoImage-3.png?raw=true)

We record the X & Y locations of those targets within the camera's field of view.

Using this location, we are able to get the yaw of the robot relative to the target and the distance from the target to the robot.
