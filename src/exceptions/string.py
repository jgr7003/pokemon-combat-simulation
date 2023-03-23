from src.core.status.constants import POKEMON_STATUS


class InvalidPokemonStatus(Exception):

    def __init__(self, status: str, message: str = f"Status %s not is valid. Possibles status: {POKEMON_STATUS}"):
        self.message = message % status
        super().__init__(self.message)
