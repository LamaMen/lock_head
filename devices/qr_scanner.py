import json
import time
import traceback

import requests
import serial

QR_URL = 'http://127.0.0.1:5000/devices/qr_reader'


def start_qr_reader():
    url = QR_URL
    while True:
        try:
            code = get_qr_code()
            print("Считано значение", code)
            data = {'qr_task': code}
            r = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            print(r.content)
            time.sleep(5)

        except Exception:
            traceback.print_exc()
            break


def get_qr_code() -> str:
    # return '71-04/21'

    with serial.Serial('/dev/ttyUSB0', 9600) as qr:
        data = b""
        current_symbol = b""
        while current_symbol != b'\r':
            data += current_symbol
            current_symbol = qr.read()

    return data.decode("utf-8")


if __name__ == '__main__':
    start_qr_reader()
