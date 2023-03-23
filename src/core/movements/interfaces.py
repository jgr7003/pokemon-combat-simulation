from abc import ABC
from typing import List
from pydantic import BaseModel

from src.core.movements.ailments.base import Ailment
from src.core.movements.categories.base import Category
from src.core.movements.targets.base import Target


class Movement(ABC):
    name: str
    base: str
    power_points: int
    type: str

    priority: bool
    critical_level: int # 0 4 a 6%, 1 12.5%, 2 50%, 3 100%

    category: Category
    target: Target


class DamageMovement:
    damage: int
    accuracy: float


class AilmentMovement:
    ailment_chance: int
    ailment: Ailment


class HitsMovement:
    max_hits: int
    min_hits: int


class TurnsMovement:
    max_turns: int
    min_turns: int


class StateChangeField(BaseModel):
    change: int
    stat: str


class StateChangeMovement:
    stat_chance: int
    stat_change: List[StateChangeField]


class DrainMovement:
    drain: int


class HealingMovement:
    healing: int
