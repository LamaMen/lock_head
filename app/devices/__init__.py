from card_scanner import CardScanner
from card_logger import CardLogger

card_scanner = CardScanner()
card_logger = CardLogger()

card_scanner.attach(card_logger)
card_scanner.run()