from src.core.movements.generations.first import *
from src.core.pokemon import Pokemon
from src.core.types.constants import *


class Bulbasaur(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS, POISON]

        self.catch_rate = 0.45

        self.ps = 45
        self.physical_attack = 49
        self.physical_defense = 49
        self.special_attack = 65
        self.special_defense = 65
        self.speed = 45


class Ivysaur(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS, POISON]

        self.catch_rate = 0.45

        self.ps = 60
        self.physical_attack = 62
        self.physical_defense = 63
        self.special_attack = 80
        self.special_defense = 80
        self.speed = 60


class Venusaur(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS, POISON]

        self.catch_rate = 0.45

        self.ps = 80
        self.physical_attack = 82
        self.physical_defense = 83
        self.special_attack = 100
        self.special_defense = 100
        self.speed = 80

        self.movements = [
            # PetalBlizzard,
            PetalDance,
            Tackle,
            Growl,
            VineWhip,
            Growth,
            # PetalBlizzard,
            LeechSeed,
            RazorLeaf,
            PoisonPowder,
            SleepPowder,
            # SeedBomb,
            TakeDown,
            # SweetScent,
            # Synthesis,
            # WorrySeed,
            DoubleEdge,
            SolarBeam,
            Roar,
            Toxic,
            # BulletSeed,
            # WorkUp,
            # SunnyDay,
            HyperBeam,
            LightScreen,
            # Protect,
            # GigaDrain,
            # Safeguard,
            SolarBeam,
            Earthquake,
            DoubleTeam,
            # SludgeBomb,
            # Facade,
            Rest,
            # Attract,
            # EnergyBall,
            # FalseSwipe,
            # Endure,
            # GigaImpact,
            Flash,
            SwordsDance,
            # SleepTalk,
            # Bulldoze,
            # GrassKnot,
            # Swagger,
            Substitute,
            Cut,
            Strength,
            # RockSmash,
            # RockClimb,
            # FrenzyPlant,
            # GrassPledge,
            # GrassyGlide,
            # TerrainPulse,
        ]


class MegaVenusaur(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.ps = 80
        self.physical_attack = 100
        self.physical_defense = 123
        self.special_attack = 122
        self.special_defense = 120
        self.speed = 80


class Charmander(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE]

        self.catch_rate = 0.45

        self.ps = 39
        self.physical_attack = 52
        self.physical_defense = 43
        self.special_attack = 60
        self.special_defense = 50
        self.speed = 65


class Charmeleon(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE]

        self.catch_rate = 0.45

        self.ps = 58
        self.physical_attack = 64
        self.physical_defense = 58
        self.special_attack = 80
        self.special_defense = 65
        self.speed = 80


class Charizard(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE, FLYING]

        self.catch_rate = 0.45

        self.ps = 78
        self.physical_attack = 84
        self.physical_defense = 78
        self.special_attack = 109
        self.special_defense = 85
        self.speed = 100

        self.movements = [
            Scratch,
            Growl,
            Ember,
            # HeatWave,
            # AirSlash,
            # DragonClaw,
            # ShadowClaw,
            WingAttack,
            # FlareBlitz,
            Ember,
            Smokescreen,
            DragonRage,
            # ScaryFace,
            # FireFang,
            # FlameBurst,
            WingAttack,
            Slash,
            Flamethrower,
            FireSpin,
            # Inferno,
            # HeatWave,
            # FlareBlitz,
            Headbutt,
            Rest,
            # Protect,
            Substitute,
            Reflect,
            Dig,
            # WillOWisp,
            # Facade,
            # BrickBreak,
            Fly,
            SeismicToss,
            # DragonTail,
            # IronTail,
            RockSlide,
            ThunderPunch,
            Toxic,
            FirePunch,
            # DragonPulse,
            Flamethrower,
            # Outrage,
            Earthquake,
            SolarBeam,
            FireBlast,
            HyperBeam,
            # Roost,
            # BlastBurnSM,
            # FirePledgeSM
        ]


class MegaCharizardX(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE, DRAGON]

        self.catch_rate = 0

        self.ps = 78
        self.physical_attack = 130
        self.physical_defense = 111
        self.special_attack = 130
        self.special_defense = 85
        self.speed = 100


class MegaCharizardY(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE, FLYING]

        self.catch_rate = 0

        self.ps = 78
        self.physical_attack = 104
        self.physical_defense = 78
        self.special_attack = 159
        self.special_defense = 115
        self.speed = 100


class Squirtle(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 0.45

        self.ps = 44
        self.physical_attack = 48
        self.physical_defense = 65
        self.special_attack = 50
        self.special_defense = 64
        self.speed = 43


class Wartortle(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 0.45

        self.ps = 59
        self.physical_attack = 63
        self.physical_defense = 80
        self.special_attack = 65
        self.special_defense = 80
        self.speed = 58


class Blastoise(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 0.45

        self.ps = 79
        self.physical_attack = 83
        self.physical_defense = 100
        self.special_attack = 85
        self.special_defense = 105
        self.speed = 78


class MegaBlastoise(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 0

        self.ps = 79
        self.physical_attack = 103
        self.physical_defense = 120
        self.special_attack = 135
        self.special_defense = 115
        self.speed = 78


class Caterpie(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [BUG]

        self.catch_rate = 2.55

        self.ps = 45
        self.physical_attack = 30
        self.physical_defense = 35
        self.special_attack = 20
        self.special_defense = 20
        self.speed = 45


class Metapod(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [BUG]

        self.catch_rate = 1.2

        self.ps = 50
        self.physical_attack = 20
        self.physical_defense = 55
        self.special_attack = 25
        self.special_defense = 25
        self.speed = 30


class Butterfree(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [BUG, FLYING]

        self.catch_rate = 0.45

        self.ps = 60
        self.physical_attack = 45
        self.physical_defense = 50
        self.special_attack = 901
        self.special_defense = 80
        self.speed = 70


class Weedle(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [BUG, POISON]

        self.catch_rate = 2.55

        self.ps = 40
        self.physical_attack = 35
        self.physical_defense = 30
        self.special_attack = 20
        self.special_defense = 20
        self.speed = 50


class Kakuna(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [BUG, POISON]

        self.catch_rate = 1.2

        self.ps = 45
        self.physical_attack = 25
        self.physical_defense = 50
        self.special_attack = 25
        self.special_defense = 25
        self.speed = 35


class Beedrill(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [BUG, POISON]

        self.catch_rate = 0.45

        self.ps = 65
        self.physical_attack = 901
        self.physical_defense = 40
        self.special_attack = 45
        self.special_defense = 80
        self.speed = 75


class MegaBeedrill(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [BUG, POISON]

        self.catch_rate = 0

        self.ps = 65
        self.physical_attack = 150
        self.physical_defense = 40
        self.special_attack = 15
        self.special_defense = 80
        self.speed = 145


class Pidgey(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL, FLYING]

        self.catch_rate = 2.55

        self.ps = 40
        self.physical_attack = 45
        self.physical_defense = 40
        self.special_attack = 35
        self.special_defense = 35
        self.speed = 56


class Pidgeotto(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL, FLYING]

        self.catch_rate = 1.2

        self.ps = 63
        self.physical_attack = 60
        self.physical_defense = 55
        self.special_attack = 50
        self.special_defense = 50
        self.speed = 71


class Pidgeot(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL, FLYING]

        self.catch_rate = 0.45

        self.ps = 83
        self.physical_attack = 80
        self.physical_defense = 75
        self.special_attack = 70
        self.special_defense = 70
        self.speed = 1012


class MegaPidgeot(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL, FLYING]

        self.catch_rate = 0

        self.ps = 83
        self.physical_attack = 80
        self.physical_defense = 80
        self.special_attack = 135
        self.special_defense = 80
        self.speed = 121


class Rattata(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL]

        self.catch_rate = 2.55

        self.ps = 30
        self.physical_attack = 56
        self.physical_defense = 35
        self.special_attack = 25
        self.special_defense = 35
        self.speed = 72


class RattataAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL, DARK]

        self.catch_rate = 2.55

        self.ps = 30
        self.physical_attack = 56
        self.physical_defense = 35
        self.special_attack = 25
        self.special_defense = 35
        self.speed = 72


class Raticate(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL]

        self.catch_rate = 1.27

        self.ps = 55
        self.physical_attack = 81
        self.physical_defense = 60
        self.special_attack = 50
        self.special_defense = 70
        self.speed = 97


class RaticateAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL, DARK]

        self.catch_rate = 1.27

        self.ps = 75
        self.physical_attack = 71
        self.physical_defense = 70
        self.special_attack = 40
        self.special_defense = 80
        self.speed = 77


class Spearow(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.ps = 40
        self.physical_attack = 60
        self.physical_defense = 30
        self.special_attack = 31
        self.special_defense = 31
        self.speed = 70


class Fearow(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL, FLYING]

        self.catch_rate = 2.55

        self.ps = 65
        self.physical_attack = 90
        self.physical_defense = 65
        self.special_attack = 61
        self.special_defense = 61
        self.speed = 100


class Ekans(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON]

        self.catch_rate = 2.55

        self.ps = 35
        self.physical_attack = 60
        self.physical_defense = 44
        self.special_attack = 40
        self.special_defense = 54
        self.speed = 55


class Arbok(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON]

        self.catch_rate = 0.90

        self.ps = 60
        self.physical_attack = 953
        self.physical_defense = 69
        self.special_attack = 65
        self.special_defense = 79
        self.speed = 80


class Pikachu(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ELECTRIC]

        self.catch_rate = 1.90

        self.ps = 35
        self.physical_attack = 55
        self.physical_defense = 404
        self.special_attack = 50
        self.special_defense = 505
        self.speed = 90


class Raichu(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ELECTRIC]

        self.catch_rate = 0.75

        self.ps = 60
        self.physical_attack = 90
        self.physical_defense = 55
        self.special_attack = 90
        self.special_defense = 80
        self.speed = 1106


class RaichuAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ELECTRIC, PSYCHIC]

        self.catch_rate = 0.75

        self.ps = 60
        self.physical_attack = 85
        self.physical_defense = 50
        self.special_attack = 95
        self.special_defense = 85
        self.speed = 110


class Sandshrew(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GROUND]

        self.catch_rate = 2.55

        self.ps = 50
        self.physical_attack = 75
        self.physical_defense = 85
        self.special_attack = 20
        self.special_defense = 30
        self.speed = 40


class SandshrewAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ICE, STEEL]

        self.catch_rate = 2.55

        self.ps = 50
        self.physical_attack = 75
        self.physical_defense = 90
        self.special_attack = 10
        self.special_defense = 35
        self.speed = 40


class Sandslash(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GROUND]

        self.catch_rate = 0.90

        self.ps = 75
        self.physical_attack = 100
        self.physical_defense = 110
        self.special_attack = 45
        self.special_defense = 55
        self.speed = 65


class SandslashAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ICE, STEEL]

        self.catch_rate = 0.90

        self.ps = 75
        self.physical_attack = 100
        self.physical_defense = 120
        self.special_attack = 25
        self.special_defense = 65
        self.speed = 65


class NidoranFemale(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON]

        self.catch_rate = 2.35

        self.ps = 55
        self.physical_attack = 47
        self.physical_defense = 52
        self.special_attack = 40
        self.special_defense = 40
        self.speed = 41


class Nidorina(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON]

        self.catch_rate = 1.20

        self.ps = 70
        self.physical_attack = 62
        self.physical_defense = 67
        self.special_attack = 55
        self.special_defense = 55
        self.speed = 56


class Nidoqueen(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON, GROUND]

        self.catch_rate = 0.45

        self.ps = 90
        self.physical_attack = 927
        self.physical_defense = 87
        self.special_attack = 75
        self.special_defense = 85
        self.speed = 76


class NidoranMale(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON]

        self.catch_rate = 2.35

        self.ps = 46
        self.physical_attack = 57
        self.physical_defense = 40
        self.special_attack = 40
        self.special_defense = 40
        self.speed = 50


class Nidorino(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON]

        self.catch_rate = 1.20

        self.ps = 61
        self.physical_attack = 72
        self.physical_defense = 57
        self.special_attack = 55
        self.special_defense = 55
        self.speed = 65


class Nidoking(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON, GROUND]

        self.catch_rate = 0.45

        self.ps = 81
        self.physical_attack = 1028
        self.physical_defense = 77
        self.special_attack = 85
        self.special_defense = 75
        self.speed = 85


class Clefairy(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FAIRY]

        self.catch_rate = 1.5

        self.ps = 70
        self.physical_attack = 45
        self.physical_defense = 48
        self.special_attack = 60
        self.special_defense = 65
        self.speed = 35


class Clefable(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FAIRY]

        self.catch_rate = 0.25

        self.ps = 95
        self.physical_attack = 70
        self.physical_defense = 73
        self.special_attack = 959
        self.special_defense = 90
        self.speed = 60


class Vulpix(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE]

        self.catch_rate = 1.90

        self.ps = 38
        self.physical_attack = 41
        self.physical_defense = 40
        self.special_attack = 50
        self.special_defense = 65
        self.speed = 65


class VulpixAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ICE]

        self.catch_rate = 1.90

        self.ps = 38
        self.physical_attack = 41
        self.physical_defense = 40
        self.special_attack = 50
        self.special_defense = 65
        self.speed = 65


class Ninetales(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE]

        self.catch_rate = 0.75

        self.ps = 73
        self.physical_attack = 76
        self.physical_defense = 75
        self.special_attack = 81
        self.special_defense = 100
        self.speed = 100


class NinetalesAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ICE, FAIRY]

        self.catch_rate = 0.75

        self.ps = 73
        self.physical_attack = 67
        self.physical_defense = 75
        self.special_attack = 81
        self.special_defense = 100
        self.speed = 109


class Jigglypuff(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL, FAIRY]

        self.catch_rate = 1.7

        self.ps = 115
        self.physical_attack = 45
        self.physical_defense = 20
        self.special_attack = 45
        self.special_defense = 25
        self.speed = 20


class Wigglytuff(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL, FAIRY]

        self.catch_rate = 0.5

        self.ps = 140
        self.physical_attack = 70
        self.physical_defense = 45
        self.special_attack = 8510
        self.special_defense = 50
        self.speed = 45


class Zubat(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON, FLYING]

        self.catch_rate = 2.55

        self.ps = 40
        self.physical_attack = 45
        self.physical_defense = 35
        self.special_attack = 30
        self.special_defense = 40
        self.speed = 55


class Golbat(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON, FLYING]

        self.catch_rate = 0.90

        self.ps = 75
        self.physical_attack = 80
        self.physical_defense = 70
        self.special_attack = 65
        self.special_defense = 75
        self.speed = 90


class Oddish(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS, POISON]

        self.catch_rate = 2.55

        self.ps = 45
        self.physical_attack = 50
        self.physical_defense = 55
        self.special_attack = 75
        self.special_defense = 65
        self.speed = 30


class Gloom(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS, POISON]

        self.catch_rate = 1.2

        self.ps = 60
        self.physical_attack = 65
        self.physical_defense = 70
        self.special_attack = 85
        self.special_defense = 75
        self.speed = 40


class Vileplume(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS, POISON]

        self.catch_rate = 0.45

        self.ps = 75
        self.physical_attack = 80
        self.physical_defense = 85
        self.special_attack = 1106
        self.special_defense = 90
        self.speed = 50


class Paras(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS, BUG]

        self.catch_rate = 1.9

        self.ps = 35
        self.physical_attack = 70
        self.physical_defense = 55
        self.special_attack = 45
        self.special_defense = 55
        self.speed = 25


class Parasect(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS, BUG]

        self.catch_rate = 0.75

        self.ps = 60
        self.physical_attack = 95
        self.physical_defense = 80
        self.special_attack = 60
        self.special_defense = 80
        self.speed = 30


class Venonat(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON, BUG]

        self.catch_rate = 1.90

        self.ps = 60
        self.physical_attack = 55
        self.physical_defense = 50
        self.special_attack = 40
        self.special_defense = 55
        self.speed = 45


class Venomoth(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON, BUG]

        self.catch_rate = 0.75

        self.ps = 70
        self.physical_attack = 65
        self.physical_defense = 60
        self.special_attack = 90
        self.special_defense = 75
        self.speed = 90


class Diglett(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GROUND]

        self.catch_rate = 2.55

        self.ps = 10
        self.physical_attack = 55
        self.physical_defense = 25
        self.special_attack = 35
        self.special_defense = 45
        self.speed = 95


class DiglettAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GROUND, STEEL]

        self.catch_rate = 2.55

        self.ps = 10
        self.physical_attack = 55
        self.physical_defense = 30
        self.special_attack = 35
        self.special_defense = 45
        self.speed = 90


class Dugtrio(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GROUND]

        self.catch_rate = 0.50

        self.ps = 35
        self.physical_attack = 10011
        self.physical_defense = 50
        self.special_attack = 50
        self.special_defense = 70
        self.speed = 120


class DugtrioAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GROUND, STEEL]

        self.catch_rate = 0.50

        self.ps = 35
        self.physical_attack = 100
        self.physical_defense = 60
        self.special_attack = 50
        self.special_defense = 70
        self.speed = 110


class Meowth(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL]

        self.catch_rate = 2.55

        self.ps = 40
        self.physical_attack = 45
        self.physical_defense = 35
        self.special_attack = 40
        self.special_defense = 40
        self.speed = 90


class MeowthAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [DARK]

        self.catch_rate = 2.55

        self.ps = 40
        self.physical_attack = 35
        self.physical_defense = 35
        self.special_attack = 50
        self.special_defense = 40
        self.speed = 90


class Persian(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL]

        self.catch_rate = 0.90

        self.ps = 65
        self.physical_attack = 70
        self.physical_defense = 60
        self.special_attack = 65
        self.special_defense = 65
        self.speed = 115


class PersianAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [DARK]

        self.catch_rate = 0.90

        self.ps = 65
        self.physical_attack = 60
        self.physical_defense = 60
        self.special_attack = 75
        self.special_defense = 65
        self.speed = 115


class Psyduck(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 1.9

        self.ps = 50
        self.physical_attack = 52
        self.physical_defense = 48
        self.special_attack = 65
        self.special_defense = 50
        self.speed = 55


class Golduck(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 0.75

        self.ps = 80
        self.physical_attack = 82
        self.physical_defense = 78
        self.special_attack = 95
        self.special_defense = 80
        self.speed = 85


class Mankey(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIGHTING]

        self.catch_rate = 1.9

        self.ps = 40
        self.physical_attack = 80
        self.physical_defense = 35
        self.special_attack = 35
        self.special_defense = 45
        self.speed = 70


class Primeape(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIGHTING]

        self.catch_rate = 0.75

        self.ps = 65
        self.physical_attack = 105
        self.physical_defense = 60
        self.special_attack = 60
        self.special_defense = 70
        self.speed = 95


class Growlithe(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE]

        self.catch_rate = 1.90

        self.ps = 55
        self.physical_attack = 70
        self.physical_defense = 45
        self.special_attack = 70
        self.special_defense = 50
        self.speed = 60


class Arcanine(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE]

        self.catch_rate = 0.75

        self.ps = 90
        self.physical_attack = 110
        self.physical_defense = 80
        self.special_attack = 100
        self.special_defense = 80
        self.speed = 95


class Poliwag(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 2.55

        self.ps = 40
        self.physical_attack = 50
        self.physical_defense = 40
        self.special_attack = 40
        self.special_defense = 40
        self.speed = 90


class Poliwhirl(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 1.2

        self.ps = 65
        self.physical_attack = 65
        self.physical_defense = 65
        self.special_attack = 50
        self.special_defense = 50
        self.speed = 90


class Poliwrath(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER, FIGHTING]

        self.catch_rate = 0.45

        self.ps = 90
        self.physical_attack = 959
        self.physical_defense = 95
        self.special_attack = 70
        self.special_defense = 90
        self.speed = 70


class Abra(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [PSYCHIC]

        self.catch_rate = 2

        self.ps = 25
        self.physical_attack = 20
        self.physical_defense = 15
        self.special_attack = 105
        self.special_defense = 55
        self.speed = 90


class Kadabra(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [PSYCHIC]

        self.catch_rate = 1

        self.ps = 40
        self.physical_attack = 35
        self.physical_defense = 30
        self.special_attack = 120
        self.special_defense = 70
        self.speed = 105


class Alakazam(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [PSYCHIC]

        self.catch_rate = 0.5

        self.ps = 55
        self.physical_attack = 50
        self.physical_defense = 45
        self.special_attack = 135
        self.special_defense = 959
        self.speed = 120


class MegaAlakazam(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [PSYCHIC]

        self.catch_rate = 0

        self.ps = 55
        self.physical_attack = 50
        self.physical_defense = 65
        self.special_attack = 175
        self.special_defense = 10512
        self.speed = 150


class Machop(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIGHTING]

        self.catch_rate = 1.8

        self.ps = 70
        self.physical_attack = 80
        self.physical_defense = 50
        self.special_attack = 35
        self.special_defense = 35
        self.speed = 35


class Machoke(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIGHTING]

        self.catch_rate = 0.9

        self.ps = 80
        self.physical_attack = 100
        self.physical_defense = 70
        self.special_attack = 50
        self.special_defense = 60
        self.speed = 45


class Machamp(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIGHTING]

        self.catch_rate = 0.45

        self.ps = 90
        self.physical_attack = 130
        self.physical_defense = 80
        self.special_attack = 65
        self.special_defense = 85
        self.speed = 55


class Bellsprout(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS, POISON]

        self.catch_rate = 2.55

        self.ps = 50
        self.physical_attack = 75
        self.physical_defense = 35
        self.special_attack = 70
        self.special_defense = 30
        self.speed = 40


class Weepinbell(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS, POISON]

        self.catch_rate = 1.2

        self.ps = 65
        self.physical_attack = 90
        self.physical_defense = 50
        self.special_attack = 85
        self.special_defense = 45
        self.speed = 55


class Victreebel(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS, POISON]

        self.catch_rate = 0.45

        self.ps = 80
        self.physical_attack = 105
        self.physical_defense = 65
        self.special_attack = 100
        self.special_defense = 7013
        self.speed = 70


class Tentacool(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER, POISON]

        self.catch_rate = 1.9

        self.ps = 40
        self.physical_attack = 40
        self.physical_defense = 35
        self.special_attack = 50
        self.special_defense = 100
        self.speed = 70


class Tentacruel(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER, POISON]

        self.catch_rate = 0.6

        self.ps = 80
        self.physical_attack = 70
        self.physical_defense = 65
        self.special_attack = 80
        self.special_defense = 120
        self.speed = 100


class Geodude(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ROCK, GROUND]

        self.catch_rate = 2.55

        self.ps = 40
        self.physical_attack = 80
        self.physical_defense = 100
        self.special_attack = 30
        self.special_defense = 30
        self.speed = 20


class GeodudeAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ROCK, ELECTRIC]

        self.catch_rate = 2.55

        self.ps = 40
        self.physical_attack = 80
        self.physical_defense = 100
        self.special_attack = 30
        self.special_defense = 30
        self.speed = 20


class Graveler(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ROCK, GROUND]

        self.catch_rate = 1.2

        self.ps = 55
        self.physical_attack = 95
        self.physical_defense = 115
        self.special_attack = 45
        self.special_defense = 45
        self.speed = 35


class GravelerAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ROCK, ELECTRIC]

        self.catch_rate = 1.2

        self.ps = 55
        self.physical_attack = 95
        self.physical_defense = 115
        self.special_attack = 45
        self.special_defense = 45
        self.speed = 35


class Golem(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ROCK, GROUND]

        self.catch_rate = 0.45

        self.ps = 80
        self.physical_attack = 12014
        self.physical_defense = 130
        self.special_attack = 55
        self.special_defense = 65
        self.speed = 45


class GolemAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ROCK, ELECTRIC]

        self.catch_rate = 0.45

        self.ps = 80
        self.physical_attack = 120
        self.physical_defense = 130
        self.special_attack = 55
        self.special_defense = 65
        self.speed = 45


class Ponyta(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE]

        self.catch_rate = 1.9

        self.ps = 50
        self.physical_attack = 85
        self.physical_defense = 55
        self.special_attack = 65
        self.special_defense = 65
        self.speed = 90


class Rapidash(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE]

        self.catch_rate = 0.6

        self.ps = 65
        self.physical_attack = 100
        self.physical_defense = 70
        self.special_attack = 80
        self.special_defense = 80
        self.speed = 105


class Slowpoke(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER, PSYCHIC]

        self.catch_rate = 1.9

        self.ps = 90
        self.physical_attack = 65
        self.physical_defense = 65
        self.special_attack = 40
        self.special_defense = 40
        self.speed = 15


class Slowbro(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER, PSYCHIC]

        self.catch_rate = 0.75

        self.ps = 95
        self.physical_attack = 75
        self.physical_defense = 110
        self.special_attack = 100
        self.special_defense = 80
        self.speed = 30


class MegaSlowbro(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER, PSYCHIC]

        self.catch_rate = 0

        self.ps = 95
        self.physical_attack = 75
        self.physical_defense = 180
        self.special_attack = 130
        self.special_defense = 80
        self.speed = 30


class Magnemite(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ELECTRIC, STEEL]

        self.catch_rate = 1.9

        self.ps = 25
        self.physical_attack = 35
        self.physical_defense = 70
        self.special_attack = 95
        self.special_defense = 55
        self.speed = 45


class Magneton(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ELECTRIC, STEEL]

        self.catch_rate = 0.6

        self.ps = 50
        self.physical_attack = 60
        self.physical_defense = 95
        self.special_attack = 120
        self.special_defense = 70
        self.speed = 70


class Farfetchd(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL, FLYING]

        self.catch_rate = 0.45

        self.ps = 52
        self.physical_attack = 9015
        self.physical_defense = 55
        self.special_attack = 58
        self.special_defense = 62
        self.speed = 60


class Doduo(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL, FLYING]

        self.catch_rate = 1.9

        self.ps = 35
        self.physical_attack = 85
        self.physical_defense = 45
        self.special_attack = 35
        self.special_defense = 35
        self.speed = 75


class Dodrio(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL, FLYING]

        self.catch_rate = 0.45

        self.ps = 60
        self.physical_attack = 110
        self.physical_defense = 70
        self.special_attack = 60
        self.special_defense = 60
        self.speed = 11016


class Seel(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 1.9

        self.ps = 65
        self.physical_attack = 45
        self.physical_defense = 55
        self.special_attack = 45
        self.special_defense = 70
        self.speed = 45


class Dewgong(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER, ICE]

        self.catch_rate = 0.75

        self.ps = 90
        self.physical_attack = 70
        self.physical_defense = 80
        self.special_attack = 70
        self.special_defense = 95
        self.speed = 70


class Grimer(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON]

        self.catch_rate = 1.9

        self.ps = 80
        self.physical_attack = 80
        self.physical_defense = 50
        self.special_attack = 40
        self.special_defense = 50
        self.speed = 25


class GrimerAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON, DARK]

        self.catch_rate = 1.9

        self.ps = 80
        self.physical_attack = 80
        self.physical_defense = 50
        self.special_attack = 40
        self.special_defense = 50
        self.speed = 25


class Muk(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON]

        self.catch_rate = 0.75

        self.ps = 105
        self.physical_attack = 105
        self.physical_defense = 75
        self.special_attack = 65
        self.special_defense = 100
        self.speed = 50


class MukAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON, DARK]

        self.catch_rate = 0.75

        self.ps = 105
        self.physical_attack = 105
        self.physical_defense = 75
        self.special_attack = 65
        self.special_defense = 100
        self.speed = 50


class Shellder(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 1.9

        self.ps = 30
        self.physical_attack = 65
        self.physical_defense = 100
        self.special_attack = 45
        self.special_defense = 25
        self.speed = 40


class Cloyster(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 0.6

        self.ps = 50
        self.physical_attack = 95
        self.physical_defense = 180
        self.special_attack = 85
        self.special_defense = 45
        self.speed = 70


class Gastly(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GHOST, POISON]

        self.catch_rate = 1.9

        self.ps = 30
        self.physical_attack = 35
        self.physical_defense = 30
        self.special_attack = 100
        self.special_defense = 35
        self.speed = 80


class Haunter(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GHOST, POISON]

        self.catch_rate = 0.9

        self.ps = 45
        self.physical_attack = 50
        self.physical_defense = 45
        self.special_attack = 115
        self.special_defense = 55
        self.speed = 95


class Gengar(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GHOST, POISON]

        self.catch_rate = 0.45

        self.ps = 60
        self.physical_attack = 65
        self.physical_defense = 60
        self.special_attack = 130
        self.special_defense = 75
        self.speed = 110


class MegaGengar(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GHOST, POISON]

        self.catch_rate = 0

        self.ps = 60
        self.physical_attack = 65
        self.physical_defense = 80
        self.special_attack = 170
        self.special_defense = 95
        self.speed = 130


class Onix(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ROCK, GROUND]

        self.catch_rate = 0.45

        self.ps = 35
        self.physical_attack = 45
        self.physical_defense = 160
        self.special_attack = 30
        self.special_defense = 45
        self.speed = 70


class Drowzee(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [PSYCHIC]

        self.catch_rate = 1.9

        self.ps = 60
        self.physical_attack = 48
        self.physical_defense = 45
        self.special_attack = 43
        self.special_defense = 90
        self.speed = 42


class Hypno(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [PSYCHIC]

        self.catch_rate = 0.75

        self.ps = 85
        self.physical_attack = 73
        self.physical_defense = 70
        self.special_attack = 73
        self.special_defense = 115
        self.speed = 67


class Krabby(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 2.25

        self.ps = 30
        self.physical_attack = 105
        self.physical_defense = 90
        self.special_attack = 25
        self.special_defense = 25
        self.speed = 50


class Kingler(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 0.6

        self.ps = 55
        self.physical_attack = 130
        self.physical_defense = 115
        self.special_attack = 50
        self.special_defense = 50
        self.speed = 75


class Voltorb(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ELECTRIC]

        self.catch_rate = 1.9

        self.ps = 40
        self.physical_attack = 30
        self.physical_defense = 50
        self.special_attack = 55
        self.special_defense = 55
        self.speed = 100


class Electrode(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ELECTRIC]

        self.catch_rate = 0.6

        self.ps = 60
        self.physical_attack = 50
        self.physical_defense = 70
        self.special_attack = 80
        self.special_defense = 80
        self.speed = 15017


class Exeggcute(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS, PSYCHIC]

        self.catch_rate = 0.9

        self.ps = 60
        self.physical_attack = 40
        self.physical_defense = 80
        self.special_attack = 60
        self.special_defense = 45
        self.speed = 40


class Exeggutor(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS, PSYCHIC]

        self.catch_rate = 0.45

        self.ps = 95
        self.physical_attack = 95
        self.physical_defense = 85
        self.special_attack = 125
        self.special_defense = 7518
        self.speed = 55


class ExeggutorAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS, DRAGON]

        self.catch_rate = 0.45

        self.ps = 95
        self.physical_attack = 105
        self.physical_defense = 85
        self.special_attack = 125
        self.special_defense = 75
        self.speed = 45


class Cubone(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GROUND]

        self.catch_rate = 1.9

        self.ps = 50
        self.physical_attack = 50
        self.physical_defense = 95
        self.special_attack = 40
        self.special_defense = 50
        self.speed = 35


class Marowak(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GROUND]

        self.catch_rate = 0.75

        self.ps = 60
        self.physical_attack = 80
        self.physical_defense = 110
        self.special_attack = 50
        self.special_defense = 80
        self.speed = 45


class MarowakAlola(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE, GHOST]

        self.catch_rate = 0.75

        self.ps = 60
        self.physical_attack = 80
        self.physical_defense = 110
        self.special_attack = 50
        self.special_defense = 80
        self.speed = 45


class Hitmonlee(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIGHTING]

        self.catch_rate = 0.45

        self.ps = 50
        self.physical_attack = 120
        self.physical_defense = 53
        self.special_attack = 35
        self.special_defense = 110
        self.speed = 87


class Hitmonchan(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIGHTING]

        self.catch_rate = 0.45

        self.ps = 50
        self.physical_attack = 105
        self.physical_defense = 79
        self.special_attack = 35
        self.special_defense = 110
        self.speed = 76


class Lickitung(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL]

        self.catch_rate = 0.45

        self.ps = 90
        self.physical_attack = 55
        self.physical_defense = 75
        self.special_attack = 60
        self.special_defense = 75
        self.speed = 30


class Koffing(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON]

        self.catch_rate = 1.9

        self.ps = 40
        self.physical_attack = 65
        self.physical_defense = 95
        self.special_attack = 60
        self.special_defense = 45
        self.speed = 35


class Weezing(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [POISON]

        self.catch_rate = 0.6

        self.ps = 65
        self.physical_attack = 90
        self.physical_defense = 120
        self.special_attack = 85
        self.special_defense = 70
        self.speed = 60


class Rhyhorn(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GROUND, ROCK]

        self.catch_rate = 1.2

        self.ps = 80
        self.physical_attack = 85
        self.physical_defense = 95
        self.special_attack = 30
        self.special_defense = 30
        self.speed = 25


class Rhydon(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GROUND, ROCK]

        self.catch_rate = 0.6

        self.ps = 105
        self.physical_attack = 130
        self.physical_defense = 120
        self.special_attack = 45
        self.special_defense = 45
        self.speed = 40


class Chansey(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL]

        self.catch_rate = 0.3

        self.ps = 250
        self.physical_attack = 5
        self.physical_defense = 5
        self.special_attack = 35
        self.special_defense = 105
        self.speed = 50


class Tangela(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [GRASS]

        self.catch_rate = 0.45

        self.ps = 65
        self.physical_attack = 55
        self.physical_defense = 115
        self.special_attack = 100
        self.special_defense = 40
        self.speed = 60


class Kangaskhan(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL]

        self.catch_rate = 0.45

        self.ps = 105
        self.physical_attack = 95
        self.physical_defense = 80
        self.special_attack = 40
        self.special_defense = 80
        self.speed = 90


class MegaKangaskhan(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL]

        self.catch_rate = 0

        self.ps = 105
        self.physical_attack = 125
        self.physical_defense = 100
        self.special_attack = 60
        self.special_defense = 100
        self.speed = 100


class Horsea(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 2.25

        self.ps = 30
        self.physical_attack = 40
        self.physical_defense = 70
        self.special_attack = 70
        self.special_defense = 25
        self.speed = 60


class Seadra(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 0.75

        self.ps = 55
        self.physical_attack = 65
        self.physical_defense = 95
        self.special_attack = 95
        self.special_defense = 45
        self.speed = 85


class Goldeen(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 2.25

        self.ps = 45
        self.physical_attack = 67
        self.physical_defense = 60
        self.special_attack = 35
        self.special_defense = 50
        self.speed = 63


class Seaking(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 0.60

        self.ps = 80
        self.physical_attack = 92
        self.physical_defense = 65
        self.special_attack = 65
        self.special_defense = 80
        self.speed = 68


class Staryu(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 2.25

        self.ps = 30
        self.physical_attack = 45
        self.physical_defense = 55
        self.special_attack = 70
        self.special_defense = 55
        self.speed = 85


class Starmie(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER, PSYCHIC]

        self.catch_rate = 0.60

        self.ps = 60
        self.physical_attack = 75
        self.physical_defense = 85
        self.special_attack = 100
        self.special_defense = 85
        self.speed = 115


class MrMime(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FAIRY, PSYCHIC]

        self.catch_rate = 0.45

        self.ps = 40
        self.physical_attack = 45
        self.physical_defense = 65
        self.special_attack = 100
        self.special_defense = 120
        self.speed = 90


class Scyther(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [BUG, FLYING]

        self.catch_rate = 0.45

        self.ps = 70
        self.physical_attack = 110
        self.physical_defense = 80
        self.special_attack = 55
        self.special_defense = 80
        self.speed = 105


class Jynx(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ICE, PSYCHIC]

        self.catch_rate = 0.45

        self.ps = 65
        self.physical_attack = 50
        self.physical_defense = 35
        self.special_attack = 115
        self.special_defense = 95
        self.speed = 95


class Electabuzz(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ELECTRIC]

        self.catch_rate = 0.45

        self.ps = 65
        self.physical_attack = 83
        self.physical_defense = 57
        self.special_attack = 95
        self.special_defense = 85
        self.speed = 105


class Magmar(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE]

        self.catch_rate = 0.45

        self.ps = 65
        self.physical_attack = 95
        self.physical_defense = 57
        self.special_attack = 100
        self.special_defense = 85
        self.speed = 93


class Pinsir(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [BUG]

        self.catch_rate = 0.45

        self.ps = 65
        self.physical_attack = 125
        self.physical_defense = 100
        self.special_attack = 55
        self.special_defense = 70
        self.speed = 85


class MegaPinsir(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [BUG, FLYING]

        self.catch_rate = 0

        self.ps = 65
        self.physical_attack = 155
        self.physical_defense = 120
        self.special_attack = 65
        self.special_defense = 90
        self.speed = 105


class Tauros(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL]

        self.catch_rate = 0.45

        self.ps = 75
        self.physical_attack = 100
        self.physical_defense = 95
        self.special_attack = 40
        self.special_defense = 70
        self.speed = 110


class Magikarp(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 2.55

        self.ps = 20
        self.physical_attack = 10
        self.physical_defense = 55
        self.special_attack = 15
        self.special_defense = 20
        self.speed = 80


class Gyarados(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER, FLYING]

        self.catch_rate = 0.45

        self.ps = 95
        self.physical_attack = 125
        self.physical_defense = 79
        self.special_attack = 60
        self.special_defense = 100
        self.speed = 81


class MegaGyarados(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER, DARK]

        self.catch_rate = 0

        self.ps = 95
        self.physical_attack = 155
        self.physical_defense = 109
        self.special_attack = 70
        self.special_defense = 130
        self.speed = 81


class Lapras(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER, ICE]

        self.catch_rate = 0.45

        self.ps = 130
        self.physical_attack = 85
        self.physical_defense = 80
        self.special_attack = 85
        self.special_defense = 95
        self.speed = 60


class Ditto(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL]

        self.catch_rate = 0.35

        self.ps = 48
        self.physical_attack = 48
        self.physical_defense = 48
        self.special_attack = 48
        self.special_defense = 48
        self.speed = 48


class Eevee(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL]

        self.catch_rate = 0.45

        self.ps = 55
        self.physical_attack = 55
        self.physical_defense = 50
        self.special_attack = 45
        self.special_defense = 65
        self.speed = 55


class Vaporeon(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [WATER]

        self.catch_rate = 0.45

        self.ps = 130
        self.physical_attack = 65
        self.physical_defense = 60
        self.special_attack = 110
        self.special_defense = 95
        self.speed = 65


class Jolteon(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ELECTRIC]

        self.catch_rate = 0.45

        self.ps = 65
        self.physical_attack = 65
        self.physical_defense = 60
        self.special_attack = 110
        self.special_defense = 95
        self.speed = 130


class Flareon(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE]

        self.catch_rate = 0.45

        self.ps = 65
        self.physical_attack = 130
        self.physical_defense = 60
        self.special_attack = 95
        self.special_defense = 110
        self.speed = 65


class Porygon(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL]

        self.catch_rate = 0.45

        self.ps = 65
        self.physical_attack = 60
        self.physical_defense = 70
        self.special_attack = 85
        self.special_defense = 75
        self.speed = 40


class Omanyte(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ROCK, WATER]

        self.catch_rate = 0.45

        self.ps = 35
        self.physical_attack = 40
        self.physical_defense = 100
        self.special_attack = 90
        self.special_defense = 55
        self.speed = 35


class Omastar(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ROCK, WATER]

        self.catch_rate = 0.45

        self.ps = 70
        self.physical_attack = 60
        self.physical_defense = 125
        self.special_attack = 115
        self.special_defense = 70
        self.speed = 55


class Kabuto(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ROCK, WATER]

        self.catch_rate = 0.45

        self.ps = 30
        self.physical_attack = 80
        self.physical_defense = 90
        self.special_attack = 55
        self.special_defense = 45
        self.speed = 55


class Kabutops(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ROCK, WATER]

        self.catch_rate = 0.45

        self.ps = 60
        self.physical_attack = 115
        self.physical_defense = 105
        self.special_attack = 65
        self.special_defense = 70
        self.speed = 80


class Aerodactyl(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ROCK, FLYING]

        self.catch_rate = 0.45

        self.ps = 80
        self.physical_attack = 105
        self.physical_defense = 65
        self.special_attack = 60
        self.special_defense = 75
        self.speed = 130


class MegaAerodactyl(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ROCK, FLYING]

        self.catch_rate = 0

        self.ps = 80
        self.physical_attack = 135
        self.physical_defense = 85
        self.special_attack = 70
        self.special_defense = 95
        self.speed = 150


class Snorlax(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [NORMAL]

        self.catch_rate = 0.25

        self.ps = 160
        self.physical_attack = 110
        self.physical_defense = 65
        self.special_attack = 65
        self.special_defense = 110
        self.speed = 30


class Articuno(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ICE, FLYING]

        self.catch_rate = 0.03

        self.ps = 90
        self.physical_attack = 85
        self.physical_defense = 100
        self.special_attack = 95
        self.special_defense = 125
        self.speed = 85


class Zapdos(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [ELECTRIC, FLYING]

        self.catch_rate = 0.03

        self.ps = 90
        self.physical_attack = 90
        self.physical_defense = 85
        self.special_attack = 125
        self.special_defense = 90
        self.speed = 100


class Moltres(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [FIRE, FLYING]

        self.catch_rate = 0.03

        self.ps = 90
        self.physical_attack = 100
        self.physical_defense = 90
        self.special_attack = 125
        self.special_defense = 85
        self.speed = 90


class Dratini(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [DRAGON]

        self.catch_rate = 0.45

        self.ps = 41
        self.physical_attack = 64
        self.physical_defense = 45
        self.special_attack = 50
        self.special_defense = 50
        self.speed = 50


class Dragonair(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [DRAGON]

        self.catch_rate = 0.45

        self.ps = 61
        self.physical_attack = 84
        self.physical_defense = 65
        self.special_attack = 70
        self.special_defense = 70
        self.speed = 70


class Dragonite(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [DRAGON, FLYING]

        self.catch_rate = 0.45

        self.ps = 91
        self.physical_attack = 134
        self.physical_defense = 95
        self.special_attack = 100
        self.special_defense = 100
        self.speed = 80


class Mewtwo(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [PSYCHIC]

        self.catch_rate = 0.03

        self.ps = 106
        self.physical_attack = 110
        self.physical_defense = 90
        self.special_attack = 154
        self.special_defense = 90
        self.speed = 130


class MegaMewtwoX(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [PSYCHIC, FIGHTING]

        self.catch_rate = 0.03

        self.ps = 106
        self.physical_attack = 190
        self.physical_defense = 100
        self.special_attack = 154
        self.special_defense = 100
        self.speed = 130


class MegaMewtwoY(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [PSYCHIC]

        self.catch_rate = 0.03

        self.ps = 106
        self.physical_attack = 150
        self.physical_defense = 70
        self.special_attack = 194
        self.special_defense = 120
        self.speed = 140


class Mew(Pokemon):

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = [PSYCHIC]

        self.catch_rate = 0.45

        self.ps = 100
        self.physical_attack = 100
        self.physical_defense = 100
        self.special_attack = 100
        self.special_defense = 100
        self.speed = 100


