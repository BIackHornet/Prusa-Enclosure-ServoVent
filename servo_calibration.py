# Run this script from terminal on a pc to manually locate duty cycle for angle

from machine import Pin, PWM
from time import sleep

# Setup servo
servo_pin = 0  # Change if needed
servo = PWM(Pin(servo_pin))
servo.freq(50)

# Starting duty cycle (try middle)
duty = 5000
step = 50  # How much to increase/decrease per keypress

def set_duty(d):
    servo.duty_u16(d)
    print(f"Set duty_u16: {d}")

set_duty(duty)

print("Servo Calibration Started")
print("Use 'a' to decrease, 'd' to increase, 'q' to quit\n")

while True:
    key = input("Command (a/d/q): ").strip().lower()
    if key == 'a':
        duty = max(0, duty - step)
        set_duty(duty)
    elif key == 'd':
        duty = min(65535, duty + step)
        set_duty(duty)
    elif key == 'q':
        print("Exiting and releasing PWM.")
        break
    else:
        print("Invalid input. Use 'a', 'd', or 'q'.")

# Turn off PWM when done
servo.deinit()