from smbus import SMBus

ARDUINO_I2C_ADDRESS = 0x8


def open_slot(slot_number):
    bus = SMBus(1)
    bus.write_byte(ARDUINO_I2C_ADDRESS, slot_number)
    bus.close()
    # print('open slot ' + str(slot_number))
