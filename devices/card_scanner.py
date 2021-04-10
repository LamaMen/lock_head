import serial

import time

import requests
import json

CARD_URL = 'http://127.0.0.1:5000/devices/card_reader'


def start_card_scanner():
    url = CARD_URL
    while True:
        try:
            data = {'card': get_card_number()}
            r = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            time.sleep(10)
        except Exception:
            break


def get_card_number() -> str:
    # return '12354'
    with serial.Serial('/dev/serial0', 9600) as card:
        data = b''
        current_byte = b''
        while current_byte != b'\x03':
            if current_byte != b'\x02':
                data += current_byte
            current_byte = card.read()

    return str(int(data[2:-2], 16))


if __name__ == '__main__':
    start_card_scanner()
