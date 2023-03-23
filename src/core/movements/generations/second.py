from src.core.movements.constants import *
from src.core.pokemon import Pokemon
from src.core.types.constants import *


class Aeroblast:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FLYING
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 100
        self.accuracy = 95
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class AncientPower:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ROCK
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 60
        self.accuracy = 100
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Attract:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class BatonPass:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 40

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class BeatUp:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = DARK
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class BellyDrum:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class BoneRush:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GROUND
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 25
        self.accuracy = 90
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Charm:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FAIRY
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Conversion2:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class CottonSpore:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GRASS
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 40

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class CrossChop:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 100
        self.accuracy = 80
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Crunch:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = DARK
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 80
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Curse:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GHOST
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class DestinyBond:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GHOST
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Detect:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class DragonBreath:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = DRAGON
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 60
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class DynamicPunch:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 100
        self.accuracy = 50
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Encore:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Endure:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class ExtremeSpeed:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 80
        self.accuracy = 100
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class FalseSwipe:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 40

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class FeintAttack:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = DARK
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 60
        self.accuracy = 0
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Flail:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class FlameWheel:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIRE
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 60
        self.accuracy = 100
        self.power_points = 25

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Foresight:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 40

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Frustration:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class FuryCutter:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = BUG
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 40
        self.accuracy = 95
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class FutureSight:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 120
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class GigaDrain:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GRASS
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 75
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class HealBell:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class HiddenPower:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 60
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class IcyWind:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ICE
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 55
        self.accuracy = 95
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class IronTail:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = STEEL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 100
        self.accuracy = 75
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class LockOn:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class MachPunch:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Magnitude:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GROUND
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 100
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class MeanLook:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Megahorn:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = BUG
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 120
        self.accuracy = 85
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class MetalClaw:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = STEEL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 50
        self.accuracy = 95
        self.power_points = 35

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class MilkDrink:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class MindReader:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class MirrorCoat:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 0
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Moonlight:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FAIRY
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class MorningSun:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class MudSlap:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GROUND
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 20
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Nightmare:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GHOST
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Octazooka:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = WATER
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 65
        self.accuracy = 85
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Outrage:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = DRAGON
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 120
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class PainSplit:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class PerishSong:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class PowderSnow:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ICE
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 25

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Present:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 90
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Protect:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class PsychUp:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Pursuit:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = DARK
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class RainDance:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = WATER
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class RapidSpin:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 50
        self.accuracy = 100
        self.power_points = 40

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Return:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Reversal:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class RockSmash:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Rollout:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ROCK
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 30
        self.accuracy = 90
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SacredFire:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIRE
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 100
        self.accuracy = 95
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Safeguard:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 25

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Sandstorm:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ROCK
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class ScaryFace:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class ShadowBall:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GHOST
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 80
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Sketch:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 1

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SleepTalk:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SludgeBomb:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = POISON
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 90
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Snore:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 50
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Spark:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ELECTRIC
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 65
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SpiderWeb:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = BUG
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Spikes:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GROUND
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Spite:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GHOST
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SteelWing:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = STEEL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 70
        self.accuracy = 90
        self.power_points = 25

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SunnyDay:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIRE
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Swagger:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 85
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SweetKiss:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FAIRY
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 75
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SweetScent:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Synthesis:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GRASS
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Thief:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = DARK
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 60
        self.accuracy = 100
        self.power_points = 25

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class TripleKick:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 10
        self.accuracy = 90
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Twister:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = DRAGON
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class VitalThrow:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 70
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Whirlpool:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = WATER
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 35
        self.accuracy = 85
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class ZapCannon:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ELECTRIC
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 120
        self.accuracy = 50
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


