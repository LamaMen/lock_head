import time
import traceback

import RPi.GPIO as GPIO
import requests


def start_button():
    button_pin = 12

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    url = 'http://127.0.0.1:5000/devices/button'
    while True:
        try:
            button_state = GPIO.input(button_pin)
            if not button_state:
                print('Button clicked')
                r = requests.get(url)
                print(r.content)
                time.sleep(10)

        except Exception:
            traceback.print_exc()
            break


if __name__ == '__main__':
    start_button()
