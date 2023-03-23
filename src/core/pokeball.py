from random import randint
from typing import List

from src.exceptions.list import PokeballRangeException, DefineRangeFirst


class Pokeballs:
    name: str
    _range: List[int]
    n: int

    def __init__(self):
        self.name = self.__class__.__name__
        self.generate_range()

    @property
    def range(self) -> List[int]:
        return self._range

    @range.setter
    def range(self, value):
        if len(value) != 2:
            raise PokeballRangeException
        self._range = value

    def generate_range(self):
        between = self._range
        print(f"Pokeball range: {between}")
        try:
            self.n = randint(between[0], between[1])
        except IndexError:
            raise DefineRangeFirst
        print(f"Pokeball n: {self.n}")


class Pokeball(Pokeballs):

    def __init__(self):
        self.range = [0, 255]
        super().__init__()


class GreatBall(Pokeballs):

    def __init__(self):
        self.range = [0, 200]
        super().__init__()


class UltraBall(Pokeballs):

    def __init__(self):
        self.range = [0, 150]
        super().__init__()


class MasterBall(Pokeballs):

    def __init__(self):
        self.range = [0, 25]
        super().__init__()
