from devices.gpio_helper import GPIOHelper
from devices.slots_handler import open_slot
from services.box_service import BoxService
from services.log_service import LogService


class DeviceHelper:
    worker = ""
    qr_code = ""
    is_worker_login = False
    is_qr_code_input = False
    led = GPIOHelper()

    def set_worker(self, worker):
        if not self.is_worker_login:
            self.worker = worker
            self.is_worker_login = True
            self.led.card_turn_on()

        self.open_slot()

    def set_qr_code(self, qr_code):
        if not self.is_qr_code_input:
            self.qr_code = qr_code
            self.is_qr_code_input = True
            self.led.qr_turn_on()

        self.open_slot()

    def is_ready(self):
        return self.is_worker_login and self.is_qr_code_input

    def open_slot(self):
        if self.is_ready():
            LogService.add_log(self.worker, self.qr_code)
            box_number = self.get_box_number()

            if box_number != -1:
                open_slot(box_number)

            self.reset()

    def reset(self):
        self.is_worker_login = False
        self.is_qr_code_input = False
        self.led.turn_off_all()

    def get_box_number(self):
        boxes = BoxService.show_all()
        box_number = -1
        for box in boxes:
            if box.tech_task_id == self.qr_code:
                box_number = box.box_id

        return box_number
