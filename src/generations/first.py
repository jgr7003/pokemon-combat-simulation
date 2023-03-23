from src.core.pokemon import Pokemon


class Pikachu(Pokemon):

    def __init__(self) -> None:
        super().__init__()
        self.catch_rate = 0.35

    def set_status(self, status: str) -> None:
        self.status = status
