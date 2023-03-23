from src.core.pokemon import Pokemon
from abc import ABC, abstractmethod


class Category(ABC):

    @abstractmethod
    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass


class Damage(Category):

    def __init__(self):
        self.name = "Damage"
        self.description = "Inflicts damage"

    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass


class Ailment(Category):

    def __init__(self):
        self.name = "Ailment"
        self.description = "No damage; inflicts status ailment"

    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass


class NetGoodStats(Category):

    def __init__(self):
        self.name = "Net Good Stats"
        self.description = "No damage; lowers target's stats or raises user's stats"

    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass


class Heal(Category):

    def __init__(self):
        self.name = "Heal"
        self.description = "No damage; heals the user"

    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass


class DamageAilment(Category):

    def __init__(self):
        self.name = "Damage Ailment"
        self.description = "Inflicts damage; inflicts status ailment"

    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass


class Swagger(Category):

    def __init__(self):
        self.name = "Swagger"
        self.description = "No damage; inflicts status ailment; raises target's stats"

    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass


class DamageLower(Category):

    def __init__(self):
        self.name = "Damage Lower"
        self.description = "Inflicts damage; lowers target's stats"

    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass


class DamageRaise(Category):

    def __init__(self):
        self.name = "Damage Raise"
        self.description = "Inflicts damage; raises user's stats"

    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass


class DamageHeal(Category):

    def __init__(self):
        self.name = "Damage Heal"
        self.description = "Inflicts damage; absorbs damage done to heal the user"

    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass


class Ohko(Category):

    def __init__(self):
        self.name = "Ohko"
        self.description = "One-hit KO"

    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass


class WholeFieldEffect(Category):

    def __init__(self):
        self.name = "Whole Field Effect"
        self.description = "Effect on the whole field"

    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass


class FieldEffect(Category):

    def __init__(self):
        self.name = "Field Effect"
        self.description = "Effect on one side of the field"

    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass


class ForceSwitch(Category):

    def __init__(self):
        self.name = "Force Switch"
        self.description = "Forces target to switch out"

    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass


class Unique(Category):

    def __init__(self):
        self.name = "Unique"
        self.description = "Unique effect"

    def execute(self, attacker: Pokemon, defender: Pokemon, movement):
        pass
