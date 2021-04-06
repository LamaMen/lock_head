from observer import Observer
from subject import Subject
from typing import List
from threading import Thread
import serial


class CardScanner(Subject, Thread):
    _card_number: int = None
    _observers: List[Observer] = []

    def run(self) -> None:
        while True:
            _data = self.get_card_number()
            self._card_number = int(_data[2:-2], 16)
            self.notify()

    @staticmethod
    def get_card_number() -> str:
        with serial.Serial('/dev/serial0', 9600) as card:
            data = b''
            current_byte = b''
            while current_byte != b'\x03':
                if current_byte != b'\x02':
                    data += current_byte
                current_byte = card.read()

        return str(data)

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._card_number)
