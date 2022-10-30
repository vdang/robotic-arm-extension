def put_claw_in_default_position():
    global claw_angle_min, claw_angle_max, claw_angle_default, claw_angle
    claw_angle_min = 60
    claw_angle_max = 160
    claw_angle_default = 90
    claw_angle = claw_angle_default
    pins.servo_write_pin(AnalogPin.P8, claw_angle)
def reset_robotic_arm():
    global mid_angle, top_angle, base_angle
    while mid_angle < mid_angle_default:
        mid_angle += 5
        pins.servo_write_pin(AnalogPin.P2, mid_angle)
        basic.pause(200)
    put_middle_arm_in_default_position()
    basic.pause(200)
    while abs(top_angle - top_angle_default) > 5:
        if top_angle >= top_angle_default:
            top_angle += -5
        else:
            top_angle += 5
        pins.servo_write_pin(AnalogPin.P1, top_angle)
        basic.pause(200)
    put_top_arm_in_default_position()
    basic.pause(200)
    while abs(base_angle - base_angle_default) > 5:
        if base_angle >= base_angle_default:
            base_angle += -5
        else:
            base_angle += 5
        pins.servo_write_pin(AnalogPin.P9, base_angle)
        basic.pause(200)
    put_base_in_default_position()
    basic.pause(200)
    put_claw_in_default_position()
def lower_top_arm():
    global top_angle
    if top_angle < top_angle_max:
        top_angle += angle_step
        pins.servo_write_pin(AnalogPin.P1, top_angle)

def on_bluetooth_connected():
    reset_robotic_arm()
    bluetooth.start_uart_service()
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.yawn),
        SoundExpressionPlayMode.UNTIL_DONE)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    reset_robotic_arm()
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.sad),
        SoundExpressionPlayMode.UNTIL_DONE)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def put_top_arm_in_default_position():
    global top_angle_min, top_angle_max, top_angle_default, top_angle
    top_angle_min = 10
    top_angle_max = 180
    top_angle_default = 90
    top_angle = top_angle_default
    pins.servo_write_pin(AnalogPin.P1, top_angle)
def put_middle_arm_in_default_position():
    global mid_angle_min, mid_angle_max, mid_angle_default, mid_angle
    mid_angle_min = 90
    mid_angle_max = 170
    mid_angle_default = 170
    mid_angle = mid_angle_default
    pins.servo_write_pin(AnalogPin.P2, mid_angle)
def lift_middle_arm():
    global mid_angle
    if mid_angle < mid_angle_max:
        mid_angle += angle_step
        pins.servo_write_pin(AnalogPin.P2, mid_angle)
def put_base_in_default_position():
    global base_angle_min, base_angle_max, base_angle_default, base_angle
    base_angle_min = 10
    base_angle_max = 170
    base_angle_default = 100
    base_angle = base_angle_default
    pins.servo_write_pin(AnalogPin.P9, base_angle)
def put_robotic_arm_in_starting_position():
    global angle_step, claw_angle_step
    angle_step = 3
    claw_angle_step = 10
    put_claw_in_default_position()
    basic.pause(500)
    put_top_arm_in_default_position()
    basic.pause(500)
    put_middle_arm_in_default_position()
    basic.pause(500)
    put_base_in_default_position()
def lower_middle_arm():
    global mid_angle
    if mid_angle > mid_angle_min:
        mid_angle += 0 - angle_step
        pins.servo_write_pin(AnalogPin.P2, mid_angle)

def on_uart_data_received():
    global cmd
    cmd = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
    if cmd == "C+":
        open_claw()
    elif cmd == "C-":
        close_claw()
    elif cmd == "T+":
        lift_top_arm()
    elif cmd == "T-":
        lower_top_arm()
    elif cmd == "M+":
        lift_middle_arm()
    elif cmd == "M-":
        lower_middle_arm()
    elif cmd == "R":
        reset_robotic_arm()
    elif cmd == "B+":
        rotate_base_right()
    elif cmd == "B-":
        rotate_base_left()
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.HASH), on_uart_data_received)

def rotate_base_right():
    global base_angle
    if base_angle > base_angle_min:
        base_angle += 0 - angle_step
        pins.servo_write_pin(AnalogPin.P9, base_angle)
def close_claw():
    global claw_angle
    if claw_angle < claw_angle_max:
        claw_angle += claw_angle_step
        pins.servo_write_pin(AnalogPin.P8, claw_angle)
def rotate_base_left():
    global base_angle
    if base_angle < base_angle_max:
        base_angle += angle_step
        pins.servo_write_pin(AnalogPin.P9, base_angle)
def lift_top_arm():
    global top_angle
    if top_angle > top_angle_min:
        top_angle += 0 - angle_step
        pins.servo_write_pin(AnalogPin.P1, top_angle)
def open_claw():
    global claw_angle
    if claw_angle > claw_angle_max:
        claw_angle += 0 - claw_angle_step
        pins.servo_write_pin(AnalogPin.P8, claw_angle)
cmd = ""
claw_angle_step = 0
base_angle_max = 0
base_angle_min = 0
mid_angle_max = 0
mid_angle_min = 0
top_angle_min = 0
angle_step = 0
top_angle_max = 0
base_angle_default = 0
base_angle = 0
top_angle_default = 0
top_angle = 0
mid_angle_default = 0
mid_angle = 0
claw_angle = 0
claw_angle_default = 0
claw_angle_max = 0
claw_angle_min = 0
put_robotic_arm_in_starting_position()
music.play_sound_effect(music.builtin_sound_effect(soundExpression.spring),
    SoundExpressionPlayMode.UNTIL_DONE)