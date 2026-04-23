# my_bot

ROS 2 simulation package for an autonomous indoor patrol robot that follows a yellow path in a custom Gazebo house world.

## Overview

This project combines:

- a custom indoor Gazebo world with rooms, walls, furniture, and a visible yellow route
- a differential-drive robot described with Xacro/URDF
- a camera sensor mounted on the robot
- a Python ROS 2 node that performs vision-based path following

The robot subscribes to `/camera/image_raw`, detects yellow pixels in the lower region of the image, estimates the path center, and publishes velocity commands to `/cmd_vel` to stay aligned with the route.

## Features

- Gazebo simulation of a house-like indoor environment
- Differential-drive robot with odometry and camera support
- OpenCV-based yellow path detection
- Proportional steering control for smooth tracking
- Search behavior when the path is temporarily lost
- ROS 2 launch files for spawning the robot and starting the simulation

## Project Structure

```text
my_bot/
├── config/
├── description/
│   ├── robot_core.xacro
│   ├── camera.xacro
│   ├── gazebo_control.xacro
│   └── robot.urdf.xacro
├── launch/
│   ├── rsp.launch.py
│   └── launch_sim.launch.py
├── my_bot/
│   └── path_follower.py
├── worlds/
│   └── patrol_house.world
├── package.xml
├── setup.py
└── README.md
```

## Requirements

- ROS 2 Humble or compatible ROS 2 distribution
- Gazebo and `gazebo_ros`
- Python 3
- OpenCV
- `cv_bridge`
- `numpy`

## Installation

1. Clone or place the package inside your ROS 2 workspace `src` folder.
2. Build the workspace:

```bash
colcon build --symlink-install
```

3. Source the workspace:

```bash
source install/setup.bash
```

## Run the Simulation

Launch the full simulation with the robot, world, and path follower:

```bash
ros2 launch my_bot launch_sim.launch.py
```

If needed, you can also launch only the robot state publisher:

```bash
ros2 launch my_bot rsp.launch.py
```

## How It Works

1. `launch_sim.launch.py` starts Gazebo with `worlds/patrol_house.world`.
2. `rsp.launch.py` publishes the robot description generated from Xacro.
3. The robot is spawned into the simulation using `spawn_entity.py`.
4. `path_follower.py` listens to the camera topic, detects the yellow path, and sends `Twist` commands to `/cmd_vel`.

## Algorithm Summary

- Convert the camera image from ROS format to OpenCV format.
- Crop the lower part of the frame as the region of interest.
- Convert the ROI to HSV color space.
- Threshold the yellow path.
- Clean the mask using morphological operations.
- Find the largest contour and compute its centroid.
- Use proportional control to steer the robot back to the path center.


## License

Apache-2.0

## Acknowledgement

This project was developed as part of the Mobile and Autonomous Robots course mini-project.
