from typing import List

from src.core.movements.interfaces import Movement
from src.core.status.constants import *
from src.core.status.strategies import *
from src.exceptions.numeric import CatchRateException
from src.exceptions.string import InvalidPokemonStatus


class Pokemon(ABC):
    name: str
    type: List[str]

    _catch_rate: float
    _status: str

    ps: int
    physical_attack: int
    physical_defense: int
    special_attack: int
    special_defense: int
    speed: int

    movements = List[Movement]

    def __init__(self) -> None:
        self.name = self.__class__.__name__
        self.status = None

    @property
    def catch_rate(self) -> float:
        return self._catch_rate

    @catch_rate.setter
    def catch_rate(self, value: float) -> None:
        if 0 > value > 1:
            raise CatchRateException
        self._catch_rate = value

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        if value is not None and value not in POKEMON_STATUS:
            raise InvalidPokemonStatus(value)
        self._status = value

    def catch_attempt(self, pokeball: Pokeballs) -> bool:
        # You can overwrite this method if the Pokemon has special conditions to be caught
        catch = False
        if self.status is not None:
            status_affected_strategy_map = {
                POISONED: Poisoned,
                PARALYZED: Paralyzed,
                ASLEEP: Asleep,
                FROZEN: Frozen,
                BURNED: Burned
            }
            status_strategy = status_affected_strategy_map[self.status]()
            print(f"Status strategy selected {type(status_strategy)}")
            catch = status_strategy.catch_effect(pokeball)
            print(f"Caught from status strategy: {catch}")

        # When not was caught by status effect
        if catch is False:
            try:
                modified_catch = float(25 / pokeball.n)
            except ZeroDivisionError:
                modified_catch = float(1)

            print(f"Modifier catch: {modified_catch}")
            modified_catch += self.catch_rate
            print(f"Modifier catch plus rate: {modified_catch}")
            if modified_catch > float(1):
                catch = True

        return catch

