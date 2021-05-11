import json
import time
import traceback

import requests
import serial

QR_URL = 'http://127.0.0.1:5000/devices/qr_reader'


def read_qr_number():
    code = get_qr_code()
    data = {'qr_task': code}
    requests.post(QR_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    time.sleep(5)


def get_qr_code() -> str:
    with serial.Serial('/dev/ttyUSB0', 9600) as qr:
        data = b""
        current_symbol = b""
        while current_symbol != b'\r':
            data += current_symbol
            current_symbol = qr.read()

    return data.decode("utf-8")


if __name__ == '__main__':
    while True:
        try:
            read_qr_number()
        except Exception:
            traceback.print_exc()
