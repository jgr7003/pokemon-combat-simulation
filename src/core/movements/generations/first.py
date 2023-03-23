from src.core.movements.constants import *
from src.core.movements.interfaces import AttackMovement, StatusMovement
from src.core.movements.mixins import RecoversHalfHPInflictedMixIn, MayLowerSpecialDefenseMixIn, \
    RaisesCreatureStatisticsMixIn
from src.core.pokemon import Pokemon
from src.core.types.constants import *


class Absorb(AttackMovement, RecoversHalfHPInflictedMixIn):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GRASS
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 20
        self.accuracy = 100
        self.power_points = 25


class Acid(AttackMovement, MayLowerSpecialDefenseMixIn):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = POISON
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 30
        self.effect_probability = 0.10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class AcidArmor(StatusMovement, RaisesCreatureStatisticsMixIn):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = POISON
        self.category = MOVEMENT_BASE_STATUS
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        # Sharply raises user's Defense.
        pass


class Agility(StatusMovement, RaisesCreatureStatisticsMixIn):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_STATUS
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        # Sharply raises user's Speed.
        pass


class Amnesia:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class AuroraBeam:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ICE
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 65
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Barrage:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 15
        self.accuracy = 85
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Barrier:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Bide:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Bind:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 15
        self.accuracy = 85
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Bite:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = DARK
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 60
        self.accuracy = 100
        self.power_points = 25

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Blizzard:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ICE
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 110
        self.accuracy = 70
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class BodySlam:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 85
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class BoneClub:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GROUND
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 65
        self.accuracy = 85
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Bonemerang:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GROUND
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 50
        self.accuracy = 90
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Bubble:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = WATER
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class BubbleBeam:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = WATER
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 65
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Clamp:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = WATER
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 35
        self.accuracy = 85
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class CometPunch:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 18
        self.accuracy = 85
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class ConfuseRay:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GHOST
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Confusion:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 50
        self.accuracy = 100
        self.power_points = 25

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Constrict:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 10
        self.accuracy = 100
        self.power_points = 35

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Conversion:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Counter:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class CrabHammer:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = WATER
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 100
        self.accuracy = 90
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Cut:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 50
        self.accuracy = 95
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class DefenseCurl:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 40

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Dig:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GROUND
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 80
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Disable:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class DizzyPunch:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 70
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class DoubleKick:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 30
        self.accuracy = 100
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class DoubleSlap:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 15
        self.accuracy = 85
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class DoubleTeam:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class DoubleEdge:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 120
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class DragonRage:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = DRAGON
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 0
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class DreamEater:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 100
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class DrillPeck:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FLYING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 80
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Earthquake:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GROUND
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 100
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class EggBomb:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 100
        self.accuracy = 75
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Ember:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIRE
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 25

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Explosion:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 250
        self.accuracy = 100
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class FireBlast:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIRE
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 110
        self.accuracy = 85
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class FirePunch:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIRE
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 75
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class FireSpin:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIRE
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 35
        self.accuracy = 85
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Fissure:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GROUND
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 30
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Flamethrower:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIRE
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 90
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Flash:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Fly:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FLYING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 90
        self.accuracy = 95
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class FocusEnergy:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class FuryAttack:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 15
        self.accuracy = 85
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class FurySwipes:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 18
        self.accuracy = 80
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Glare:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Growl:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 40

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Growth:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Guillotine:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 30
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Gust:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FLYING
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 35

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Harden:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Haze:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ICE
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Headbutt:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 70
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class HighJumpKick:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 130
        self.accuracy = 90
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class HornAttack:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 65
        self.accuracy = 100
        self.power_points = 25

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class HornDrill:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 30
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class HydroPump:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = WATER
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 110
        self.accuracy = 80
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class HyperBeam:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 150
        self.accuracy = 90
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class HyperFang:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 80
        self.accuracy = 90
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Hypnosis:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 60
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class IceBeam:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ICE
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 90
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class IcePunch:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ICE
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 75
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class JumpKick:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 100
        self.accuracy = 95
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class KarateChop:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 50
        self.accuracy = 100
        self.power_points = 25

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Kinesis:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 80
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class LeechLife:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = BUG
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 80
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class LeechSeed:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GRASS
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 90
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Leer:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Lick:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GHOST
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 30
        self.accuracy = 100
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class LightScreen:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class LovelyKiss:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 75
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class LowKick:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Meditate:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 40

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class MegaDrain:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GRASS
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class MegaKick:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 120
        self.accuracy = 75
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class MegaPunch:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 80
        self.accuracy = 85
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Metronome:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Mimic:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Minimize:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class MirrorMove:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FLYING
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Mist:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ICE
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class NightShade:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GHOST
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 0
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class PayDay:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Peck:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FLYING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 35
        self.accuracy = 100
        self.power_points = 35

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class PetalDance:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GRASS
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 120
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class PinMissile:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = BUG
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 25
        self.accuracy = 95
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class PoisonGas:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = POISON
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 90
        self.power_points = 40

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class PoisonPowder:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = POISON
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 75
        self.power_points = 35

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class PoisonSting:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = POISON
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 15
        self.accuracy = 100
        self.power_points = 35

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Pound:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 35

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Psybeam:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 65
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Psychic:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 90
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Psywave:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 0
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class QuickAttack:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Rage:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 20
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class RazorLeaf:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GRASS
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 55
        self.accuracy = 95
        self.power_points = 25

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class RazorWind:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 80
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Recover:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Reflect:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Rest:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Roar:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class RockSlide:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ROCK
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 75
        self.accuracy = 90
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class RockThrow:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ROCK
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 50
        self.accuracy = 90
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class RollingKick:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 60
        self.accuracy = 85
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SandAttack:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GROUND
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Scratch:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 35

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Screech:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 85
        self.power_points = 40

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SeismicToss:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SelfDestruct:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 200
        self.accuracy = 100
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Sharpen:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Sing:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 55
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SkullBash:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 130
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SkyAttack:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FLYING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 140
        self.accuracy = 90
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Slam:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 80
        self.accuracy = 75
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Slash:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 70
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SleepPowder:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GRASS
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 75
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Sludge:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = POISON
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 65
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Smog:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = POISON
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 30
        self.accuracy = 70
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Smokescreen:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SoftBoiled:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 5

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SolarBeam:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GRASS
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 120
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SonicBoom:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 0
        self.accuracy = 90
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SpikeCannon:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 20
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Splash:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 40

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Spore:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GRASS
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Stomp:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 65
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Strength:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 80
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class StringShot:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = BUG
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 95
        self.power_points = 40

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Struggle:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 50
        self.accuracy = 0
        self.power_points = 1

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class StunSpore:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GRASS
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 75
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Submission:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FIGHTING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 80
        self.accuracy = 80
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Substitute:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SuperFang:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 0
        self.accuracy = 90
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Supersonic:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 55
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Surf:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = WATER
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 90
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Swift:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 60
        self.accuracy = 0
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class SwordsDance:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Tackle:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 35

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class TailWhip:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 100
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class TakeDown:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 90
        self.accuracy = 85
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Teleport:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = PSYCHIC
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Thrash:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 120
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Thunder:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ELECTRIC
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 110
        self.accuracy = 70
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class ThunderPunch:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ELECTRIC
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 75
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class ThunderShock:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ELECTRIC
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class ThunderWave:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ELECTRIC
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 90
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Thunderbolt:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = ELECTRIC
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 90
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Toxic:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = POISON
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 90
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Transform:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class TriAttack:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 80
        self.accuracy = 100
        self.power_points = 10

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Twineedle:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = BUG
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 25
        self.accuracy = 100
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class VineWhip:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = GRASS
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 45
        self.accuracy = 100
        self.power_points = 25

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class ViseGrip:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 55
        self.accuracy = 100
        self.power_points = 30

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class WaterGun:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = WATER
        self.category = MOVEMENT_BASE_SPECIAL
        self.damage = 40
        self.accuracy = 100
        self.power_points = 25

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Waterfall:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = WATER
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 80
        self.accuracy = 100
        self.power_points = 15

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Whirlwind:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class WingAttack:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = FLYING
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 60
        self.accuracy = 100
        self.power_points = 35

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Withdraw:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = WATER
        self.category = MOVEMENT_BASE_STATUS
        self.damage = 0
        self.accuracy = 0
        self.power_points = 40

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


class Wrap:
    def __init__(self):
        self.name = self.__class__.__name__
        self.type = NORMAL
        self.category = MOVEMENT_BASE_PHYSICAL
        self.damage = 15
        self.accuracy = 90
        self.power_points = 20

    def effect(self, attacker: Pokemon, defender: Pokemon):
        pass


