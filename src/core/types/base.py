from abc import ABC, abstractmethod
from src.core.types.constants import *
from typing import List


class CreatureTypeAsInterface(ABC):
    _type: str
    _percentage: float

    def __init__(self, _type: str, percentage: float):
        self._type = _type
        self.percentage = percentage

    @property
    def type(self) -> str:
        return self._type

    @property
    def percentage(self) -> float:
        return self._percentage

    @percentage.setter
    def percentage(self, value: float) -> None:
        self._percentage = value


class AsAttacker(CreatureTypeAsInterface):
    pass


class AsDefender(CreatureTypeAsInterface):
    pass


class PokemonType(ABC):
    attacker: List[AsAttacker]
    defender: List[AsDefender]

    def attack(self, damage: int, defender):
        pass


class Normal(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(ROCK, WEAK_AGAINST),
            AsAttacker(STEEL, WEAK_AGAINST),
            AsAttacker(GHOST, IMMUNE_AGAINST)
        ]
        self.defender = [
            AsDefender(GHOST, IMMUNE_TO),
            AsDefender(FIGHTING, WEAK_TO)
        ]


class Fire(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(BUG, STRONG_AGAINST),
            AsAttacker(STEEL, STRONG_AGAINST),
            AsAttacker(GRASS, STRONG_AGAINST),
            AsAttacker(ICE, STRONG_AGAINST),
            AsAttacker(WATER, WEAK_AGAINST),
            AsAttacker(FIRE, WEAK_AGAINST),
            AsAttacker(ROCK, WEAK_AGAINST),
            AsAttacker(DRAGON, WEAK_AGAINST),
        ]
        self.defender = [
            AsDefender(BUG, RESISTANT_TO),
            AsDefender(STEEL, RESISTANT_TO),
            AsDefender(FIRE, RESISTANT_TO),
            AsDefender(GRASS, RESISTANT_TO),
            AsDefender(ICE, RESISTANT_TO),
            AsDefender(GROUND, WEAK_TO),
            AsDefender(ROCK, WEAK_TO),
            AsDefender(WATER, WEAK_TO),
        ]


class Water(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(GROUND, STRONG_AGAINST),
            AsAttacker(ROCK, STRONG_AGAINST),
            AsAttacker(FIRE, STRONG_AGAINST),
            AsAttacker(WATER, WEAK_AGAINST),
            AsAttacker(GRASS, WEAK_AGAINST),
            AsAttacker(DRAGON, WEAK_AGAINST),
        ]
        self.defender = [
            AsDefender(STEEL, RESISTANT_TO),
            AsDefender(FIRE, RESISTANT_TO),
            AsDefender(WATER, RESISTANT_TO),
            AsDefender(ICE, RESISTANT_TO),
            AsDefender(ELECTRIC, WEAK_TO),
            AsDefender(GRASS, WEAK_TO),
        ]


class Grass(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(GROUND, STRONG_AGAINST),
            AsAttacker(ROCK, STRONG_AGAINST),
            AsAttacker(WATER, STRONG_AGAINST),
            AsAttacker(FLYING, WEAK_AGAINST),
            AsAttacker(POISON, WEAK_AGAINST),
            AsAttacker(BUG, WEAK_AGAINST),
            AsAttacker(STEEL, WEAK_AGAINST),
            AsAttacker(FIRE, WEAK_AGAINST),
            AsAttacker(GRASS, WEAK_AGAINST),
            AsAttacker(DRAGON, WEAK_AGAINST),
        ]
        self.defender = [
            AsDefender(GROUND, RESISTANT_TO),
            AsDefender(WATER, RESISTANT_TO),
            AsDefender(GRASS, RESISTANT_TO),
            AsDefender(ELECTRIC, RESISTANT_TO),
            AsDefender(FLYING, WEAK_TO),
            AsDefender(POISON, WEAK_TO),
            AsDefender(BUG, WEAK_TO),
            AsDefender(FIRE, WEAK_TO),
            AsDefender(ICE, WEAK_TO),
        ]


class Electric(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(FLYING, STRONG_AGAINST),
            AsAttacker(WATER, STRONG_AGAINST),
            AsAttacker(GRASS, WEAK_AGAINST),
            AsAttacker(ELECTRIC, WEAK_AGAINST),
            AsAttacker(DRAGON, WEAK_AGAINST),
            AsAttacker(GROUND, IMMUNE_AGAINST),
        ]
        self.defender = [
            AsDefender(FLYING, RESISTANT_TO),
            AsDefender(STEEL, RESISTANT_TO),
            AsDefender(ELECTRIC, RESISTANT_TO),
            AsDefender(GROUND, WEAK_TO),
        ]


class Ice(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(FLYING, STRONG_AGAINST),
            AsAttacker(GROUND, STRONG_AGAINST),
            AsAttacker(GRASS, STRONG_AGAINST),
            AsAttacker(DRAGON, STRONG_AGAINST),
            AsAttacker(STEEL, WEAK_AGAINST),
            AsAttacker(FIRE, WEAK_AGAINST),
            AsAttacker(WATER, WEAK_AGAINST),
            AsAttacker(ICE, WEAK_AGAINST),
        ]
        self.defender = [
            AsDefender(ICE, RESISTANT_TO),
            AsDefender(FIGHTING, WEAK_TO),
            AsDefender(ROCK, WEAK_TO),
            AsDefender(STEEL, WEAK_TO),
            AsDefender(FIRE, WEAK_TO),
        ]


class Fighting(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(NORMAL, STRONG_AGAINST),
            AsAttacker(ROCK, STRONG_AGAINST),
            AsAttacker(STEEL, STRONG_AGAINST),
            AsAttacker(ICE, STRONG_AGAINST),
            AsAttacker(DARK, STRONG_AGAINST),
            AsAttacker(FLYING, WEAK_AGAINST),
            AsAttacker(POISON, WEAK_AGAINST),
            AsAttacker(BUG, WEAK_AGAINST),
            AsAttacker(PSYCHIC, WEAK_AGAINST),
            AsAttacker(FAIRY, WEAK_AGAINST),
            AsAttacker(GHOST, 0),
        ]
        self.defender = [
            AsDefender(ROCK, RESISTANT_TO),
            AsDefender(BUG, RESISTANT_TO),
            AsDefender(DARK, RESISTANT_TO),
            AsDefender(FLYING, WEAK_TO),
            AsDefender(PSYCHIC, WEAK_TO),
            AsDefender(FAIRY, WEAK_TO),
        ]


class Poison(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(GRASS, STRONG_AGAINST),
            AsAttacker(FAIRY, STRONG_AGAINST),
            AsAttacker(POISON, WEAK_AGAINST),
            AsAttacker(GROUND, WEAK_AGAINST),
            AsAttacker(ROCK, WEAK_AGAINST),
            AsAttacker(GHOST, WEAK_AGAINST),
            AsAttacker(STEEL, IMMUNE_AGAINST),
        ]
        self.defender = [
            AsDefender(FIGHTING, RESISTANT_TO),
            AsDefender(POISON, RESISTANT_TO),
            AsDefender(GRASS, RESISTANT_TO),
            AsDefender(FAIRY, RESISTANT_TO),
            AsDefender(GROUND, WEAK_TO),
            AsDefender(PSYCHIC, WEAK_TO),
        ]


class Ground(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(POISON, STRONG_AGAINST),
            AsAttacker(ROCK, STRONG_AGAINST),
            AsAttacker(STEEL, STRONG_AGAINST),
            AsAttacker(FIRE, STRONG_AGAINST),
            AsAttacker(ELECTRIC, STRONG_AGAINST),
            AsAttacker(BUG, WEAK_AGAINST),
            AsAttacker(GRASS, WEAK_AGAINST),
            AsAttacker(FLYING, IMMUNE_AGAINST),
        ]
        self.defender = [
            AsDefender(POISON, RESISTANT_TO),
            AsDefender(ROCK, RESISTANT_TO),
            AsDefender(ELECTRIC, IMMUNE_AGAINST),
            AsDefender(WATER, WEAK_TO),
            AsDefender(GRASS, WEAK_TO),
            AsDefender(ICE, WEAK_TO),
        ]


class Flying(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(FIGHTING, STRONG_AGAINST),
            AsAttacker(BUG, STRONG_AGAINST),
            AsAttacker(GRASS, STRONG_AGAINST),
            AsAttacker(ROCK, WEAK_AGAINST),
            AsAttacker(STEEL, WEAK_AGAINST),
            AsAttacker(ELECTRIC, WEAK_AGAINST),
        ]
        self.defender = [
            AsDefender(GROUND, IMMUNE_TO),
            AsDefender(GRASS, RESISTANT_TO),
            AsDefender(BUG, RESISTANT_TO),
            AsDefender(FIGHTING, RESISTANT_TO),
            AsDefender(ROCK, WEAK_TO),
            AsDefender(ELECTRIC, WEAK_TO),
            AsDefender(ICE, WEAK_TO),
        ]


class Psychic(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(FIGHTING, STRONG_AGAINST),
            AsAttacker(POISON, STRONG_AGAINST),
            AsAttacker(STEEL, WEAK_AGAINST),
            AsAttacker(PSYCHIC, WEAK_AGAINST),
            AsAttacker(DARK, IMMUNE_AGAINST),
        ]
        self.defender = [
            AsDefender(FIGHTING, RESISTANT_TO),
            AsDefender(PSYCHIC, RESISTANT_TO),
            AsDefender(BUG, WEAK_TO),
            AsDefender(GHOST, WEAK_TO),
            AsDefender(DARK, WEAK_TO),
        ]


class Bug(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(GRASS, STRONG_AGAINST),
            AsAttacker(PSYCHIC, STRONG_AGAINST),
            AsAttacker(DARK, STRONG_AGAINST),
            AsAttacker(FIGHTING, WEAK_AGAINST),
            AsAttacker(FLYING, WEAK_AGAINST),
            AsAttacker(POISON, WEAK_AGAINST),
            AsAttacker(GHOST, WEAK_AGAINST),
            AsAttacker(FIRE, WEAK_AGAINST),
            AsAttacker(STEEL, WEAK_AGAINST),
            AsAttacker(FAIRY, WEAK_AGAINST),
        ]
        self.defender = [
            AsDefender(FIGHTING, RESISTANT_TO),
            AsDefender(GROUND, RESISTANT_TO),
            AsDefender(GRASS, RESISTANT_TO),
            AsDefender(FLYING, WEAK_TO),
            AsDefender(ROCK, WEAK_TO),
            AsDefender(FIRE, WEAK_TO),
        ]


class Rock(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(FLYING, STRONG_AGAINST),
            AsAttacker(BUG, STRONG_AGAINST),
            AsAttacker(FIRE, STRONG_AGAINST),
            AsAttacker(ICE, STRONG_AGAINST),
            AsAttacker(FIGHTING, WEAK_AGAINST),
            AsAttacker(GROUND, WEAK_AGAINST),
            AsAttacker(STEEL, WEAK_AGAINST),
        ]
        self.defender = [
            AsDefender(NORMAL, RESISTANT_TO),
            AsDefender(FLYING, RESISTANT_TO),
            AsDefender(POISON, RESISTANT_TO),
            AsDefender(FIRE, RESISTANT_TO),
            AsDefender(FIGHTING, WEAK_TO),
            AsDefender(GROUND, WEAK_TO),
            AsDefender(STEEL, WEAK_TO),
            AsDefender(WATER, WEAK_TO),
            AsDefender(GRASS, WEAK_TO),
        ]


class Ghost(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(GHOST, STRONG_AGAINST),
            AsAttacker(PSYCHIC, STRONG_AGAINST),
            AsAttacker(DARK, WEAK_AGAINST),
            AsAttacker(NORMAL, IMMUNE_AGAINST),
        ]
        self.defender = [
            AsDefender(POISON, RESISTANT_TO),
            AsDefender(BUG, RESISTANT_TO),
            AsDefender(NORMAL, IMMUNE_TO),
            AsDefender(FIGHTING, IMMUNE_TO),
            AsDefender(GHOST, WEAK_TO),
            AsDefender(DARK, WEAK_TO),
        ]


class Dark(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(GHOST, STRONG_AGAINST),
            AsAttacker(PSYCHIC, STRONG_AGAINST),
            AsAttacker(FIGHTING, WEAK_AGAINST),
            AsAttacker(DARK, WEAK_AGAINST),
            AsAttacker(FAIRY, WEAK_AGAINST),
        ]
        self.defender = [
            AsDefender(GHOST, RESISTANT_TO),
            AsDefender(DARK, RESISTANT_TO),
            AsDefender(PSYCHIC, IMMUNE_TO),
            AsDefender(FIGHTING, WEAK_TO),
            AsDefender(BUG, WEAK_TO),
            AsDefender(FAIRY, WEAK_TO),
        ]


class Dragon(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(DRAGON, STRONG_AGAINST),
            AsAttacker(STEEL, WEAK_AGAINST),
            AsAttacker(FAIRY, IMMUNE_AGAINST),
        ]
        self.defender = [
            AsDefender(FIRE, RESISTANT_TO),
            AsDefender(WATER, RESISTANT_TO),
            AsDefender(GRASS, RESISTANT_TO),
            AsDefender(ELECTRIC, RESISTANT_TO),
            AsDefender(FAIRY, WEAK_TO),
            AsDefender(ICE, WEAK_TO),
            AsDefender(DRAGON, WEAK_TO),
        ]


class Steel(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(ROCK, STRONG_AGAINST),
            AsAttacker(ICE, STRONG_AGAINST),
            AsAttacker(FAIRY, STRONG_AGAINST),
            AsAttacker(STEEL, WEAK_AGAINST),
            AsAttacker(FIRE, WEAK_AGAINST),
            AsAttacker(WATER, WEAK_AGAINST),
            AsAttacker(ELECTRIC, WEAK_AGAINST),
        ]
        self.defender = [
            AsDefender(NORMAL, RESISTANT_TO),
            AsDefender(FLYING, RESISTANT_TO),
            AsDefender(ROCK, RESISTANT_TO),
            AsDefender(BUG, RESISTANT_TO),
            AsDefender(STEEL, RESISTANT_TO),
            AsDefender(GRASS, RESISTANT_TO),
            AsDefender(PSYCHIC, RESISTANT_TO),
            AsDefender(ICE, RESISTANT_TO),
            AsDefender(DRAGON, RESISTANT_TO),
            AsDefender(FAIRY, RESISTANT_TO),
            AsDefender(POISON, IMMUNE_TO),
            AsDefender(FIGHTING, WEAK_TO),
            AsDefender(GROUND, WEAK_TO),
            AsDefender(FIRE, WEAK_TO),
        ]


class Fairy(PokemonType):

    def __init__(self):
        self.attacker = [
            AsAttacker(FIGHTING, STRONG_AGAINST),
            AsAttacker(DRAGON, STRONG_AGAINST),
            AsAttacker(DARK, STRONG_AGAINST),
            AsAttacker(POISON, WEAK_AGAINST),
            AsAttacker(STEEL, WEAK_AGAINST),
            AsAttacker(FIRE, WEAK_AGAINST),
        ]
        self.defender = [
            AsDefender(FIGHTING, RESISTANT_TO),
            AsDefender(BUG, RESISTANT_TO),
            AsDefender(DARK, RESISTANT_TO),
            AsDefender(DRAGON, IMMUNE_TO),
            AsDefender(POISON, WEAK_TO),
            AsDefender(STEEL, WEAK_TO),
        ]

