import uasyncio
from machine import Pin
from servo import Servo

# LED setup
led = Pin("LED", Pin.OUT)  # Onboard LED on Raspberry Pi Pico

# Servo setup using servo.py
servo = Servo(pin=0)  # Default settings: 50Hz, min_duty=1550, max_duty=7750, 0-180°

# Coroutine to blink the LED
async def blink_led():
    while True:
        led.on()
        await uasyncio.sleep(0.2)  # LED on for 0.2s
        led.off()
        await uasyncio.sleep(1.8)  # LED off for 1.8s (total cycle = 2s)

# Coroutine to move the servo
async def move_servo():
    while True:
        servo.move(0)  # Servo at 0 degrees
        await uasyncio.sleep(2)  # Wait 2s
        servo.move(90)  # Servo at 90 degrees
        await uasyncio.sleep(2)  # Wait 2s

# Main function to run all tasks
async def main():
    # Create tasks for LED and servo
    tasks = [
        uasyncio.create_task(blink_led()),
        uasyncio.create_task(move_servo())
    ]
    # Run tasks concurrently
    await uasyncio.gather(*tasks)

# Run the event loop
try:
    uasyncio.run(main())
except KeyboardInterrupt:
    print("Program stopped")
    servo.deinit()  # Clean up PWM on exit