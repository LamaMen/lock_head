import RPi.GPIO as GPIO


class GPIOHelper:
    qr_led_pin = 16
    scanner_led_pin = 18

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.qr_led_pin, GPIO.OUT)
        GPIO.setup(self.scanner_led_pin, GPIO.OUT)

    def qr_turn_on(self):
        GPIO.output(self.qr_led_pin, GPIO.HIGH)

    def card_turn_on(self):
        GPIO.output(self.scanner_led_pin, GPIO.HIGH)

    def qr_turn_off(self):
        GPIO.output(self.qr_led_pin, GPIO.LOW)

    def card_turn_off(self):
        GPIO.output(self.scanner_led_pin, GPIO.Low)

    def turn_off_all(self):
        self.card_turn_off()
        self.qr_turn_off()
