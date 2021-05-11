import json
import time
import traceback

import requests
import serial

CARD_URL = 'http://127.0.0.1:5000/devices/card_reader'


def read_card_number():
    code = get_card_number()
    data = {'card': code}
    requests.post(CARD_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    time.sleep(5)


def get_card_number() -> str:
    with serial.Serial('/dev/serial0', 9600) as card:
        data = b''
        current_byte = b''
        while current_byte != b'\x03':
            if current_byte != b'\x02':
                data += current_byte
            current_byte = card.read()

    return str(int(data[2:-2], 16))


if __name__ == '__main__':
    while True:
        try:
            read_card_number()
        except Exception:
            traceback.print_exc()
