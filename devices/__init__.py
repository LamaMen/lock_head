from devices.card_scanner import CardScanner
from devices.card_logger import CardLogger

scanner = CardScanner()
logger = CardLogger()

scanner.attach(logger)
scanner.run()
