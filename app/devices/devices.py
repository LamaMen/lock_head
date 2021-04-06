import serial

from slots_handler import open_slot

slots = {b'123': 1}


def get_qr_code():
    with serial.Serial('/dev/ttyUSB0', 9600) as qr:
        data = b""
        for i in range(3):
            data += qr.read()

    return data


def get_card_number():
    with serial.Serial('/dev/serial0', 9600) as card:
        data = b''
        current_byte = b''
        while current_byte != b'\x03':
            if current_byte != b'\x02':
                data += current_byte
            current_byte = card.read()

    return int(data[2:-2], 16)


if __name__ == '__main__':
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
