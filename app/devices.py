import serial
from smbus import SMBus

addr = 0x8
slots = { b'123' : 1 }

def get_qr_code():
    with serial.Serial('/dev/ttyUSB0', 9600) as qr:
        data = b""
        for i in range(3):
            data += qr.read()
     
    return data


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

print('Hello', 'Enter card', sep='\n')
card = get_card_number()
print('Card: ', card)
print('Enter qr')
qr = get_qr_code()
print('Qr: ', qr)
if qr in slots:
    print('Open slot')
    open_slot(slots[qr])
else:
    print('Error!')
