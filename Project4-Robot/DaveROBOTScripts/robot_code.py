import time
from robomaster import robot

def start():
    # move the robot forward from start position A
    Room1Type = "Fire"  # Fire
    Room2Type = "Person"  # person
    Room3Type = "Skip"  # Skip(poison)

    robot_ctrl.set_mode(rm_define.robot_mode_free)
    chassis_ctrl.set_trans_speed(.7)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.7)
    chassis_ctrl.move_with_distance(0, 0.83)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.set_trans_speed(.7)
    chassis_ctrl.move_with_distance(0,0.79)
    chassis_ctrl.set_trans_speed(.7)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.set_trans_speed(.7)
    chassis_ctrl.move_with_distance(0, 0.45)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.set_trans_speed(.7)
    chassis_ctrl.move_with_distance(0, 1.64)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 0.45)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 0.50)
    chassis_ctrl.move_with_distance(0, 0.11)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)
    chassis_ctrl.move_with_distance(0, 1.48)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)
    chassis_ctrl.move_with_distance(0, 0.40)
    chassis_ctrl.move_with_distance(0, 0.11)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 0.83)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.set_trans_speed(.7)
    chassis_ctrl.move_with_distance(0, 0.39)
    time.sleep(5)
    # Reset Point top of Zig Zag
    chassis_ctrl.set_trans_speed(.7)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.7)
    chassis_ctrl.move_with_distance(0, 1.45)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    time.sleep(1)


def room_type_1(room_type):
    if room_type == "Fire":
        # room start
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(+180)

        # moves into the room
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,2.17)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,2.06)

        # fire
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(+180)

        # function to fire gun after finding letter F.
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
        led_ctrl.gun_led_on()
        gun_ctrl.fire_once()
        time.sleep(2)
        gun_ctrl.stop()
        vision_ctrl.disable_detection(rm_define.vision_detection_marker)
        robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
        gimbal_ctrl.recenter()

        # move out of room
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,2.06)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,2.14)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.35)
        time.sleep(5)

        # room end
        # Reset Point D
        chassis_ctrl.move_with_distance(0, 4.94)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        time.sleep(1)
    if room_type == "Person":
        # Room Start
        gimbal_ctrl.set_rotate_speed(60)
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(+180)

        # Moves into the room
        chassis_ctrl.set_trans_speed(.5)
        chassis_ctrl.move_with_distance(0, 1.93)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.68)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.move_with_distance(0, 1.12)

        # Scan for person
        vision_ctrl.enable_detection(rm_define.vision_detection_people)
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(+180)

        def vision_recognized_people(msg):
            vision_ctrl.disable_detection(rm_define.vision_detection_people)

        # Move out of person room
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.2)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.move_with_distance(0, 1.12)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.68)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.93)

        # Take person back to start point A from door
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.8)
        chassis_ctrl.move_with_distance(0, 4.94)
        time.sleep(5)

        # Person safely at start point
        # Returning to room door
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        chassis_ctrl.set_trans_speed(.8)
        chassis_ctrl.move_with_distance(0, 4.94)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 3.85)
        time.sleep(5)

def room_type_2(room_type):
    if room_type == "Fire":
        # Room Start
        gimbal_ctrl.set_rotate_speed(60)
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(+180)

        # Moves into the room
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,2.17)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,2.06)

        # Fire detection
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(+180)

        # Function to fire gun after finding letter F.
        def vision_recognized_marker_letter_F(msg):
            vision_ctrl.enable_detection(rm_define.vision_detection_marker)
            vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
            led_ctrl.gun_led_on()
            gun_ctrl.fire_once()
            time.sleep(2)
            gun_ctrl.stop()
            vision_ctrl.disable_detection(rm_define.vision_detection_marker)
            robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
            gimbal_ctrl.recenter()

        # Move out of room
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,2.06)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,2.14)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.35)
        time.sleep(5)

    else:  # room_type == "Person"
        # Room Start
        gimbal_ctrl.set_rotate_speed(60)
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(+180)

        # Moves into the room
        chassis_ctrl.set_trans_speed(.5)
        chassis_ctrl.move_with_distance(0, 1.93)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.68)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.move_with_distance(0, 1.12)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.2)

        # Scan for person
        vision_ctrl.enable_detection(rm_define.vision_detection_people)
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(+180)

        def vision_recognized_people(msg):
            vision_ctrl.disable_detection(rm_define.vision_detection_people)

        # Move out of person room
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.2)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.move_with_distance(0, 1.12)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.68)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.93)

        # Take person back to start point A from door
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.8)
        chassis_ctrl.move_with_distance(0, 4.94)
        time.sleep(5)

        # Person safely at start point
        # Returning to room door
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        chassis_ctrl.set_trans_speed(.8)
        chassis_ctrl.move_with_distance(0, 4.94)
        time.sleep(1)


def room_type_3(room_type):
    if room_type == "Fire":
        # Room Start
        gimbal_ctrl.set_rotate_speed(60)
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(+180)

        # Moves into the room
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,1.93)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,1.68)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.move_with_distance(0,1.12)

        # Fire detection
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(+180)

        # Function to fire gun after finding letter F.
        def vision_recognized_marker_letter_F(msg):
            vision_ctrl.enable_detection(rm_define.vision_detection_marker)
            vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
            led_ctrl.gun_led_on()
            gun_ctrl.fire_once()
            time.sleep(2)
            gun_ctrl.stop()
            vision_ctrl.disable_detection(rm_define.vision_detection_marker)
            robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
            gimbal_ctrl.recenter()

        # Move out of room
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,1.12)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,1.68)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0,1.93)
        time.sleep(5)

    else:  # room_type == "Person"
        # Room Start
        gimbal_ctrl.set_rotate_speed(60)
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(+180)

        # Moves into the room
        chassis_ctrl.set_trans_speed(.5)
        chassis_ctrl.move_with_distance(0, 1.93)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.68)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.move_with_distance(0, 1.12)

        # Person detection
        vision_ctrl.enable_detection(rm_define.vision_detection_people)
        gimbal_ctrl.yaw_ctrl(-90)
        gimbal_ctrl.yaw_ctrl(+180)

        # Function to detect person
        def vision_recognized_people(msg):
            print("found you")
            print("follow me")
            vision_ctrl.disable_detection(rm_define.vision_detection_people)
            gimbal_ctrl.pitch_ctrl(0)
            gimbal_ctrl.recenter()
            media_ctrl.play_sound(rm_define.media_custom_audio_0)

        # Move out of room
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.12)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.68)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.set_trans_speed(.7)
        chassis_ctrl.move_with_distance(0, 1.93)
        time.sleep(5)

def special_movement():
    time.sleep(3)
    chassis_ctrl.set_trans_speed(.6)  # dance location
    chassis_ctrl.move_with_distance(90, .40)
    gimbal_ctrl.set_rotate_speed(80)

    # Fix for the gimbal rotation issue: using two 180-degree rotations
    gimbal_ctrl.rotate_with_degree(180)
    gimbal_ctrl.rotate_with_degree(180)

    chassis_ctrl.move_with_distance(-90, .80)
    gimbal_ctrl.rotate_with_degree(180)
    gimbal_ctrl.rotate_with_degree(180)

    chassis_ctrl.move_with_distance(90, .40)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 1.8)
    time.sleep(4)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 3.51)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)  # Back at Point A

    # LED effects
    led_ctrl.set_top_led(rm_define.armor_top_all, 1, 0, 0, rm_define.effect_breath)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 1, 0, 0, rm_define.effect_flash)

def special_dance():
    # Dance 1: Simple rotation and movement
    gimbal_ctrl.set_rotate_speed(80)
    gimbal_ctrl.rotate_with_degree(180)
    gimbal_ctrl.rotate_with_degree(180)
    chassis_ctrl.move_with_distance(90, .40)
    chassis_ctrl.move_with_distance(-90, .80)
    chassis_ctrl.move_with_distance(90, .40)

    # Dance 2: Zigzag movement
    chassis_ctrl.set_trans_speed(.6)
    for _ in range(5):
        chassis_ctrl.move_with_distance(45, .40)
        chassis_ctrl.move_with_distance(-45, .40)

    # Dance 3: Circle movement
    chassis_ctrl.set_trans_speed(.6)
    for _ in range(12):
        chassis_ctrl.move_with_distance(30, .40)

# Start the robot's movement
start()

# Move to Room 227 and perform action
chassis_ctrl.move_with_distance(0, 4)
chassis_ctrl.move_with_distance(0, 1.83)# Move from A to B
chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)  # Turn towards Room 227
room_type_1()  # Perform action for Room 227

# Move to Room 225 and perform action
chassis_ctrl.move_with_distance(0, 2.17)  # Move from C to D
chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)  # Turn towards Room 225
room_type_2()  # Perform action for Room 225

# Move to Room 224A and perform action
chassis_ctrl.move_with_distance(0, 1.93)  # Move from E to F
chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)  # Turn towards Room 224A
room_type_3()  # Perform action for Room 224A (if any)

# Perform the special movement
special_movement()

def return_trip():
    # Turn around at Point H to face towards Point G
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    time.sleep(1)

    # Move from Point H to Point G
    chassis_ctrl.move_with_distance(0, 4) 
    chassis_ctrl.move_with_distance(0, 1.2)  # Move forward for 5.2 meters
    time.sleep(1)

    # Rotate to face towards Point F
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    time.sleep(1)

    # Move from Point G to Point F
    chassis_ctrl.move_with_distance(0, 4.94)  # Move forward for 4.94 meters
    time.sleep(1)

    # Rotate to face towards the Start Position A
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    time.sleep(1)

    # Move from Point F to Start Position A
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, 0.33)  # Move forward for 20.33 meters to reach the start position
    time.sleep(1)

    # Ensure the robot is correctly oriented at the start position
    # This step may be necessary if the robot needs to face a specific direction at the start
    # chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    # time.sleep(1)

# Execute the return trip
return_trip()

# Special Dance
special_dance()