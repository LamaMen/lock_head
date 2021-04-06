from smbus import SMBus

# TODO поменяй константу
def open_slot(slot_number):
    bus = SMBus(1)
    bus.write_byte(addr, 1)
    bus.close()
