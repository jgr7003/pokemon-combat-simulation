from abc import abstractmethod, ABC

from src.core.pokeball import Pokeballs


class PokemonStatusInterface(ABC):

    @abstractmethod
    def catch_effect(self, pokeball: Pokeballs) -> bool:
        pass


class Poisoned(PokemonStatusInterface):

    def catch_effect(self, pokeball: Pokeballs) -> bool:
        return True if pokeball.n < 12 else False


class Asleep(PokemonStatusInterface):

    def catch_effect(self, pokeball: Pokeballs) -> bool:
        return True if pokeball.n < 25 else False


class Frozen(PokemonStatusInterface):

    def catch_effect(self, pokeball: Pokeballs) -> bool:
        return True if pokeball.n < 25 else False


class Paralyzed(PokemonStatusInterface):

    def catch_effect(self, pokeball: Pokeballs) -> bool:
        return True if pokeball.n < 12 else False


class Burned(PokemonStatusInterface):

    def catch_effect(self, pokeball: Pokeballs) -> bool:
        return True if pokeball.n < 12 else False
