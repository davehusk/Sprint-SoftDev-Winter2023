from robomaster import robot
import rm_define
import time

# Initialize the robot
s1 = robot.Robot()
s1.initialize(conn_type="sta")

# Define the robot control functions based on the provided commands
def set_robot_mode(mode):
    if mode == "gimbal_follow":
        s1.robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    elif mode == "chassis_follow":
        s1.robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    elif mode == "free":
        s1.robot_ctrl.set_mode(rm_define.robot_mode_free)

def move_forward(distance):
    s1.chassis_ctrl.move_with_distance(0, distance)

def rotate_clockwise(degrees):
    s1.chassis_ctrl.rotate_with_degree(rm_define.clockwise, degrees)

def rotate_anticlockwise(degrees):
    s1.chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, degrees)

def set_led_effects(effect, color=(255, 255, 255)):
    # Set LED color and effect
    s1.led_ctrl.set_top_led(rm_define.armor_top_all, *color, effect)
    s1.led_ctrl.set_bottom_led(rm_define.armor_bottom_all, *color, effect)

# Define the sequence of actions to navigate the course
def run_course():
    # Start position (Checkpoint A)
    set_robot_mode("chassis_follow")
    set_led_effects(rm_define.effect_flash, color=(0, 255, 0))  # Green for go
    move_forward(0.79)  # Move from A to B

    # Checkpoint B
    rotate_clockwise(90)  # Rotate to face Checkpoint C
    set_led_effects(rm_define.effect_flash, color=(255, 255, 0))  # Yellow for caution
    move_forward(1.64)    # Move from B to C

    # Checkpoint C
    rotate_anticlockwise(90)  # Rotate to face Checkpoint D
    set_led_effects(rm_define.effect_breath, color=(255, 0, 0))  # Red for stop
    move_forward(5.35)        # Move from C to D

    # Checkpoint D
    rotate_clockwise(90)      # Rotate to face Checkpoint E
    set_led_effects(rm_define.effect_marquee, color=(0, 0, 255))  # Blue for info
    move_forward(1.93)        # Move from D to E

    # Checkpoint E
    rotate_clockwise(90)      # Rotate to face Checkpoint F
    set_led_effects(rm_define.effect_flash, color=(255, 105, 180))  # Pink for fun
    move_forward(3.85)        # Move from E to F

    # Checkpoint F
    rotate_anticlockwise(90)  # Rotate to face Checkpoint G
    set_led_effects(rm_define.effect_breath, color=(0, 255, 255))  # Cyan for calm
    move_forward(4.94)        # Move from F to G

    # Checkpoint G
    rotate_anticlockwise(90)  # Rotate to face Checkpoint H
    set_led_effects(rm_define.effect_flash, color=(255, 140, 0))  # Orange for energy
    move_forward(5.2)         # Move from G to H

    # Return trip to start position (Checkpoint A)
    rotate_anticlockwise(180) # Rotate to face the return direction
    set_led_effects(rm_define.effect_flash, color=(255, 255, 255))  # White for end
    move_forward(19)          # Move from H to A (return trip)

# Run the course
run_course()

# Close the robot connection
s1.close()