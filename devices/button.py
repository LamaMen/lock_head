import time
import traceback

import RPi.GPIO as GPIO
import requests

button_pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
BUTTON_URL = 'http://127.0.0.1:5000/devices/button'


def read_button():
    button_state = GPIO.input(button_pin)
    if not button_state:
        print('Button clicked')
        r = requests.get(BUTTON_URL)
        print(r.content)
        time.sleep(10)


if __name__ == '__main__':
    while True:
        try:
            read_button()
        except Exception:
            traceback.print_exc()
            break
