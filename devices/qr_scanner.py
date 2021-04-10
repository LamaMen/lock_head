# import serial

import json
import time

import requests

CARD_URL = 'http://127.0.0.1:5000/devices/qr_reader'


def start_qr_reader():
    url = CARD_URL
    while True:
        try:
            data = {'qr_task': get_qr_code()}
            r = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            time.sleep(10)
        except Exception:
            break


def get_qr_code() -> str:
    return '106-04/21'

    # with serial.Serial('/dev/ttyUSB0', 9600) as qr:
    #     data = b""
    #     current_symbol = b""
    #     while current_symbol != b'\r':
    #         data += current_symbol
    #         current_symbol = qr.read()
    #
    # print(data)
    # return data


if __name__ == '__main__':
    start_qr_reader()
