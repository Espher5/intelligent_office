import time

from IntelligentOfficeError import IntelligentOfficeError
import mock.GPIO as GPIO
from mock.RTC import RTC


class IntelligentOffice:
    # Pin number definition
    INFRARED_PIN_1 = 11
    INFRARED_PIN_2 = 12
    INFRARED_PIN_3 = 13
    INFRARED_PIN_4 = 15
    RTC_PIN = 16
    SERVO_PIN = 18
    PHOTO_PIN = 22  # photoresistor
    LED_PIN = 29
    CO2_PIN = 31
    FAN_PIN = 32

    BLINDS_CLOSED = 0
    BLINDS_HALF_OPEN = 1
    BLINDS_FULLY_OPEN = 2

    LUX_MIN = 450
    LUX_MAX = 550

    def __init__(self):
        """
        Constructor
        """
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.INFRARED_PIN_1, GPIO.IN)
        GPIO.setup(self.INFRARED_PIN_2, GPIO.IN)
        GPIO.setup(self.INFRARED_PIN_3, GPIO.IN)
        GPIO.setup(self.INFRARED_PIN_4, GPIO.IN)
        GPIO.setup(self.PHOTO_PIN, GPIO.IN)
        GPIO.setup(self.SERVO_PIN, GPIO.OUT)
        GPIO.setup(self.LED_PIN, GPIO.OUT)
        GPIO.setup(self.CO2_PIN, GPIO.IN)
        GPIO.setup(self.FAN_PIN, GPIO.OUT)

        self.rtc = RTC(self.RTC_PIN)
        self.pwm = GPIO.PWM(self.SERVO_PIN, 50)
        self.pwm.start(0)

        self.blinds_status = self.BLINDS_CLOSED
        self.light_on = False
        self.vent_switch_on = False

    def check_quadrant_occupancy(self, pin: int) -> bool:
        """
        Checks whether one of the infrared distance sensor on the ceiling detects something in front of it.
        :param pin: The data pin of the sensor that is being checked (e.g., INFRARED_PIN1).
        :return: True if the infrared sensor detects something, False otherwise.
        """
        pass

    def manage_blinds_based_on_time(self) -> None:
        """
        Uses the RTC and servo motor to open/close the blinds based on current time and day.
        The system fully opens the blinds at 8:00 and fully closes them at 20:00
        each day except for Saturday and Sunday.
        """
        pass

    def manage_light_level(self) -> None:
        """
        Tries to maintain the actual light level inside the office, measure by the photoresitor,
        between LUX_MIN and LUX_MAX.

        If the actual light level is lower than LUX_MIN the system starts opening the blinds (through the servo motor)
        and stops it when the actual light level is greater than or equal to LUX_MIN. If, after the blinds are fully
        open, the actual light level is still lower than LUX_MIN, the system then turns on the smart light bulb.

        On the other hand, if the actual light level is greater than LUX_MAX, the system turns off the smart light bulb.
        If the actual light level is still greater than LUX_MAX, the system starts closing the blinds
        (through the servo motor) and stops it when the actual light level is less than or equal to LUX_MAX.

        :return:
        """
        pass

    def manage_lightbulb_based_on_occupancy(self) -> None:
        """
        Turn off the smart light bulb when the last worker leaves the office (i.e., the office is now vacant).
        Turn on the smart light when the first worker goes back into the office.
        :return:
        """
        pass

    def monitor_air_quality(self) -> None:
        """
        Use the carbon dioxide sensor to monitor the level of CO2 in the office.
        If the amount of detected CO2 is greater than or equal to 800 PPM, the system turns on the
        switch of the exhaust fan until the amount of CO2 is lower than 500 PPM.
        """
        pass

    def change_servo_angle(self, duty_cycle: float) -> None:
        """
        Changes the servo motor's angle by passing to it the corresponding PWM duty cycle signal
        :param duty_cycle: the length of the duty cycle
        """
        GPIO.output(self.SERVO_PIN, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(1)
        GPIO.output(self.SERVO_PIN, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)
