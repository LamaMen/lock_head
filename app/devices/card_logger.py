from observer import Observer


class CardLogger(Observer):
    current_card: int = None

    def update(self, data) -> None:
        self.current_card = data
