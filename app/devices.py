import serial
from smbus import SMBus

addr = 0x8
slots = { '123' : b'1' }

def get_qr_code():
    return 123


def open_slot(slot_number):
    bus = SMBus(1)
    bus.write_byte(addr, 1)
    bus.close()


def get_card_number():
    with serial.Serial('/dev/serial0', 9600) as card:
        data = b''
        current_byte = b''
        while current_byte != b'\x03':
            if current_byte != b'\x02':
                data += current_byte
            current_byte = card.read()
    
    return int(data[2:-2], 16)

