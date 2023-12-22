# RoboMaster S1 Obstacle Course Navigation Script

This README documents a Python script designed to control the RoboMaster S1 robot through a predefined obstacle course. The script was meticulously crafted by Dave Husk (dave.husk@keyin.com), utilizing precise measurements to ensure accurate navigation.

## Overview

The script enables the RoboMaster S1 to autonomously navigate an obstacle course, moving between designated checkpoints labeled A through H, and then returning to the starting position. At each checkpoint, the robot performs specific actions, including LED color changes to indicate its status.

## Features

- **Mode Setting**: The robot can switch between gimbal follow, chassis follow, and free modes.
- **Movement**: The robot can move forward a specified distance.
- **Rotation**: The robot can rotate clockwise or anticlockwise by a given number of degrees.
- **LED Effects**: The robot can change the color and effect of its LEDs at each checkpoint.
- **Autonomous Navigation**: The robot follows a set path, making turns and stops as programmed.

## Usage

1. **Initialization**: Connect the RoboMaster S1 to the RoboMaster S1 app via Wi-Fi and ensure it is calibrated and updated with the latest firmware.
2. **Running the Script**: Execute the script to start the obstacle course navigation.
3. **Observation**: Watch as the RoboMaster S1 autonomously navigates the course, with LED effects indicating its progress.

## Requirements

- RoboMaster S1 robot
- RoboMaster S1 Python SDK
- Python 3.x environment

## Script Details

The script contains functions to control the robot's movement and actions:

```python
def set_robot_mode(mode):
    # Set the robot's mode (gimbal_follow, chassis_follow, free)

def move_forward(distance):
    # Move the robot forward by a specified distance

def rotate_clockwise(degrees):
    # Rotate the robot clockwise by a specified number of degrees

def rotate_anticlockwise(degrees):
    # Rotate the robot anticlockwise by a specified number of degrees

def set_led_effects(effect, color=(255, 255, 255)):
    # Set the LED color and effect

def run_course():
    # Define the sequence of actions to navigate the course
```

## Course Layout

The obstacle course layout is as follows:

- **Start Position (Checkpoint A)**
- **Checkpoint B**: 0.79m forward from A
- **Checkpoint C**: Turn right, 1.64m forward
- **Checkpoint D**: Turn left, 5.35m forward
- **Checkpoint E**: Turn right, 1.93m forward
- **Checkpoint F**: Turn right, 3.85m forward
- **Checkpoint G**: Turn left, 4.94m forward
- **Turn Around Position (Checkpoint H)**: Turn left, 5.2m forward
- **Return Trip**: Turn around, 19m forward to return to A

## Acknowledgments

This script was created by Dave Husk using only measurements to ensure the RoboMaster S1 could accurately navigate the specified obstacle course.

## Disclaimer

The script is provided as-is, and it is recommended to test it in a safe, controlled environment before use. The creator is not responsible for any damage or issues that arise from the use of this script.

For more information on programming the RoboMaster S1 in Python, please refer to the official documentation and the RoboMaster S1 Python SDK.

___
> ## Contact
> Created by Dave Husk <dave.husk@keyin.com>
