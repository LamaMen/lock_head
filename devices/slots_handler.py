from smbus import SMBus
from devices.config import ARDUINO_I2C_ADDRESS


def open_slot(slot_number):
    bus = SMBus(1)
    bus.write_byte(ARDUINO_I2C_ADDRESS, slot_number)
    bus.close()
