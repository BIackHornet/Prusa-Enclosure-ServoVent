from machine import Pin, PWM

class Servo:
    def __init__(self, pin, freq=50, min_duty=1550, max_duty=7750, min_angle=0, max_angle=180):
        self._pin = pin
        self._freq = freq
        self._min_duty = min_duty
        self._max_duty = max_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self._pwm = PWM(Pin(pin))
        self._pwm.freq(self._freq)
        self._conversion_factor = (self._max_duty - self._min_duty) / (self.max_angle - self.min_angle)
        self.current_angle = None  # nothing has been moved yet

    def move(self, angle):
        angle = round(angle, 2)
        angle = max(self.min_angle, min(self.max_angle, angle))  # Clamp to range
        if angle == self.current_angle:
            return
        self.current_angle = angle
        duty = int((angle - self.min_angle) * self._conversion_factor) + self._min_duty
        self._pwm.duty_u16(duty)

    def move_to_min(self):
        self.move(self.min_angle)

    def move_to_max(self):
        self.move(self.max_angle)

    def deinit(self):
        self._pwm.deinit()