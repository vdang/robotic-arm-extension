namespace robotic_arm_extension {
    let claw_angle_min = 0
    let claw_angle_max = 0
    let claw_angle_default = 0
    let claw_angle = 0
    let mid_angle = 0
    let mid_angle_default = 0
    let top_angle = 0
    let top_angle_default = 0
    let base_angle = 0
    let base_angle_default = 0
    let top_angle_max = 0
    let top_angle_min = 0
    let mid_angle_min = 0
    let mid_angle_max = 0
    let base_angle_min = 0
    let base_angle_max = 0
    
    //% block
    export function putRoboticArmInStartingPosition() {
        put_claw_in_default_position()
        basic.pause(500)
        put_top_arm_in_default_position()
        basic.pause(500)
        put_middle_arm_in_default_position()
        basic.pause(500)
        put_base_in_default_position()
    }
    //% block
    export function resetRoboticArm () {
        while (mid_angle < mid_angle_default) {
            mid_angle += 5
            pins.servoWritePin(AnalogPin.P2, mid_angle)
            basic.pause(200)
        }
        put_middle_arm_in_default_position()
        basic.pause(200)
        while (Math.abs(top_angle - top_angle_default) > 5) {
            if (top_angle >= top_angle_default) {
                top_angle += -5
            } else {
                top_angle += 5
            }
            pins.servoWritePin(AnalogPin.P1, top_angle)
            basic.pause(200)
        }
        put_top_arm_in_default_position()
        basic.pause(200)
        while (Math.abs(base_angle - base_angle_default) > 5) {
            if (base_angle >= base_angle_default) {
                base_angle += -5
            } else {
                base_angle += 5
            }
            pins.servoWritePin(AnalogPin.P9, base_angle)
            basic.pause(200)
        }
        put_base_in_default_position()
        basic.pause(200)
        put_claw_in_default_position()
    }
    //% block
    //% angle_step.defl=10
    export function openClaw(angle_step: number = 10) {
        claw_angle = Math.max(claw_angle - angle_step, claw_angle_min)
        pins.servoWritePin(AnalogPin.P8, claw_angle)
    }
    //% block
    //% angle_step.defl=10
    export function closeClaw(angle_step: number = 10) {
        claw_angle = Math.min(claw_angle + angle_step, claw_angle_max)
        pins.servoWritePin(AnalogPin.P8, claw_angle)
    }
    //% block
    //% angle_step.defl=3
    export function rotateBaseLeft(angle_step: number = 3) {
        base_angle = Math.min(base_angle + angle_step, base_angle_max)
        pins.servoWritePin(AnalogPin.P9, base_angle)
    }
    //% block
    //% angle_step.defl=3
    export function rotateBaseRight(angle_step: number = 3) {
        base_angle = Math.max(base_angle - angle_step, base_angle_min)
        pins.servoWritePin(AnalogPin.P9, base_angle)
    }
    //% block
    //% angle_step.defl=3
    export function liftTopArm (angle_step: number = 3) {
        top_angle = Math.max(top_angle - angle_step, top_angle_min)
        pins.servoWritePin(AnalogPin.P1, top_angle)
    }
    //% block
    //% angle_step.defl=3
    export function lowerTopArm(angle_step: number = 3) {
        top_angle = Math.min(top_angle + angle_step, top_angle_max)
        pins.servoWritePin(AnalogPin.P1, top_angle)
    }
    //% block
    //% angle_step.defl=3
    export function liftMiddleArm(angle_step: number = 3) {
        mid_angle = Math.min(mid_angle + angle_step, mid_angle_max)
        pins.servoWritePin(AnalogPin.P2, mid_angle)
    }
    //% block
    //% angle_step.defl=3
    export function lowerMiddleArm(angle_step: number = 3) {
        mid_angle = Math.max(mid_angle - angle_step, mid_angle_min)
        pins.servoWritePin(AnalogPin.P2, mid_angle)
    }

    function put_claw_in_default_position() {
        claw_angle_min = 60
        claw_angle_max = 160
        claw_angle_default = 90
        claw_angle = claw_angle_default
        pins.servoWritePin(AnalogPin.P8, claw_angle)
    }
    function put_top_arm_in_default_position() {
        top_angle_min = 10
        top_angle_max = 180
        top_angle_default = 90
        top_angle = top_angle_default
        pins.servoWritePin(AnalogPin.P1, top_angle)
    }
    function put_middle_arm_in_default_position() {
        mid_angle_min = 90
        mid_angle_max = 170
        mid_angle_default = 170
        mid_angle = mid_angle_default
        pins.servoWritePin(AnalogPin.P2, mid_angle)
    }
    function put_base_in_default_position() {
        base_angle_min = 10
        base_angle_max = 170
        base_angle_default = 100
        base_angle = base_angle_default
        pins.servoWritePin(AnalogPin.P9, base_angle)
    }
}
