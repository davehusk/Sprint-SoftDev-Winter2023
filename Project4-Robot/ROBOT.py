# final sprint copy 2
# group number 2
# due date 12/21/23
 
 
def start(): # move the robot forward from start position A 
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
    
    # Room 227 
    
    vision_ctrl.enable_detection(rm_define.vision_detection_marker) 
    gimbal_ctrl.yaw_ctrl(-90) 
    gimbal_ctrl.yaw_ctrl(+180) 
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
    
    #def vision_recognized_marker_letter_F(msg): 
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
    
    # Reset Point D 
    
    chassis_ctrl.move_with_distance(0, 4.94) 
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90) 
    time.sleep(1) 
    
    # Room 225 
    gimbal_ctrl.set_rotate_speed(60)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker) 
    gimbal_ctrl.yaw_ctrl(-90) 
    gimbal_ctrl.yaw_ctrl(+180)
 
    # moves into the room
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
    
 
    # scan for person
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(+180)
    
    vision_ctrl.enable_detection(rm_define.vision_detection_marker) 
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F) 
    led_ctrl.gun_led_on() 
    gun_ctrl.fire_once() 
    time.sleep(2) 
    gun_ctrl.stop() 
    vision_ctrl.disable_detection(rm_define.vision_detection_marker) 
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow) 
    gimbal_ctrl.recenter() 
 
    # move out of person room
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
 
    # take person back to start point A from door
 
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 4.94)
    time.sleep(5)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, .33)
 
    # person safely at start point
    # Returning to room door
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, .33)
    time.sleep(5)
    chassis_ctrl.set_trans_speed(.8)
    chassis_ctrl.move_with_distance(0, 4.94)
 
    #chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90) 
    chassis_ctrl.set_trans_speed(.7) 
    chassis_ctrl.move_with_distance(0, 3.85) 
    time.sleep(5) 
    
    # Reset Point F 
    
    chassis_ctrl.set_trans_speed(.8) 
    chassis_ctrl.move_with_distance(0, 4.94) 
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90) 
    time.sleep(1) 
    
    # Room 224A(Poison Room)
 
    # Scan for marker 
    
    vision_ctrl.enable_detection(rm_define.vision_detection_marker) 
    gimbal_ctrl.yaw_ctrl(-90) 
    gimbal_ctrl.yaw_ctrl(+180) 
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90) 
    chassis_ctrl.set_trans_speed(.7) 
    chassis_ctrl.move_with_distance(0, 4) 
    chassis_ctrl.set_trans_speed(.7) 
    chassis_ctrl.move_with_distance(0, 1.2) 
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180) 
    time.sleep(5) 
    
    # H turn around position 
    
    chassis_ctrl.set_trans_speed(.8) 
    chassis_ctrl.move_with_distance(0, 5) 
    chassis_ctrl.set_trans_speed(.8) 
    chassis_ctrl.move_with_distance(0, 4.96) 
    time.sleep(4) 
    chassis_ctrl.set_trans_speed(.8) 
    chassis_ctrl.move_with_distance(0, 5) 
    chassis_ctrl.set_trans_speed(.8) 
    chassis_ctrl.move_with_distance(0, 3.79) 
    
    # Special dance 
    
    time.sleep(3) 
    
    chassis_ctrl_set_trans_speed(.6)  # dance location 
    chassis_ctrl.move_with_distance(90,.40)
 
    gimbal_ctrl.set_rotate_speed(80)
    gimbal_ctrl.rotate_with_degree(360)
 
    chassis_ctrl.move_with_distance(-90,.80)
    gimbal_ctrl.rotate_with_degree(360)
 
    chassis_ctrl.move_with_distance(90,.40)
    
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
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180) 
    
    # Back at Point A 
    
    led_ctrl.set_top_led
    (rm_define.armor_top_all, led_ctrl[1],led_ctrl[0],led_ctrl[0], rm_define.effect_breath) 
    
    led_ctrl.set_bottom_led
    (rm_define.armor_top_all, led_ctrl[1],led_ctrl[0],led_ctrl[0], rm_define.effect_flash, rm_define.effect_breath)
    
    