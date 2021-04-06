from app import app
from app.devices.slots_handler import open_slot


@app.route('/debug/open_slot')
def open_slot_debug():
    open_slot(1)
    return 'Slot opened!'
