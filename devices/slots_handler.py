from smbus import SMBus
from datetime import datetime

ARDUINO_I2C_ADDRESS = 0x8
last_open = datetime(1970, 1, 1)


def open_slot(slot_number):
    global last_open
    now = datetime.now()

    if (now - last_open).seconds > 5:
        last_open = now
        bus = SMBus(1)
        bus.write_byte(ARDUINO_I2C_ADDRESS, slot_number)
        bus.close()

    # print('open slot ' + str(slot_number))
