from app import app
from app.devices.slots_handler import open_slot
from app.devices import card_logger

@app.route('/debug/open_slot')
def open_slot_debug():
    open_slot(1)
    return 'Slot opened!'


@app.route('/debug/card')
def card():
    card_from_logger = card_logger.current_card
    if card_from_logger is not None:
        return card_from_logger
    else:
        return 'No card'
