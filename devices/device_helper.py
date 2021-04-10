from devices.slots_handler import open_slot


class DeviceHelper:
    worker = ""
    qr_code = ""
    is_worker_login = False
    is_qr_code_input = False

    def set_worker(self, worker):
        if not self.is_worker_login:
            self.worker = worker
            self.is_worker_login = True

        self.open_slot()

    def set_qr_code(self, qr_code):
        if not self.is_qr_code_input:
            self.qr_code = qr_code
            self.is_qr_code_input = True

        self.open_slot()

    def is_ready(self):
        return self.is_worker_login and self.is_qr_code_input

    def open_slot(self):
        if self.is_ready():
            # логирование
            # проверка номера ячейки
            open_slot(1)
            self.is_worker_login = False
            self.is_qr_code_input = False
