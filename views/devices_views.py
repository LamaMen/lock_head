from flask import request, abort

from app import app
from devices.device_helper import DeviceHelper

helper = DeviceHelper()


@app.route('/devices/card_reader', methods=['POST'])
def card_reader():
    if request.method == 'POST':
        card_json = request.get_json()
        card = card_json['card']
        app.logger.warning("Получено значение карты: " + card)
        helper.set_worker(card)
        return 'success', 200
    else:
        abort(400)


@app.route('/devices/qr_reader', methods=['POST'])
def qr_reader():
    if request.method == 'POST':
        qr_json = request.get_json()
        qr_code = qr_json['qr_task']
        app.logger.warning("Получено значение qr кода: " + qr_code)
        helper.set_qr_code(qr_code)
        return 'success', 200
    else:
        abort(400)
