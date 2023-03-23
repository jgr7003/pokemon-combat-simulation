from abc import ABC


class Target(ABC):
    pass


class SpecificMove(Target):
    def __init__(self):
        self.name = "Specific Move"
        self.description = "One specific move.  How this move is chosen depends upon on the move being used."


class SelectedPokemonMeFirst(Target):
    def __init__(self):
        self.name = "Selected Pokemon Me First"
        self.description = "One other Pokémon on the field, selected by the trainer. Stolen moves reuse the same target."


class Ally(Target):
    def __init__(self):
        self.name = "Ally"
        self.description = "The user's ally (if any)."


class UsersField(Target):
    def __init__(self):
        self.name = "Users Field"
        self.description = "The user's side of the field. Affects the user and its ally (if any)."


class UserOrAlly(Target):
    def __init__(self):
        self.name = "User Or Ally"
        self.description = "Either the user or its ally, selected by the trainer."


class OpponentsField(Target):
    def __init__(self):
        self.name = "Opponents Field"
        self.description = "The opposing side of the field.  Affects opposing Pokemon."


class User(Target):
    def __init__(self):
        self.name = "User"
        self.description = "The user."


class RandomOpponent(Target):
    def __init__(self):
        self.name = "Random Opponent"
        self.description = "One opposing Pokemon, selected at random."


class AllOtherPokemon(Target):
    def __init__(self):
        self.name = "All Other Pokemon"
        self.description = "Every other Pokemon on the field."


class SelectedPokemon(Target):
    def __init__(self):
        self.name = "Selected Pokemon"
        self.description = "One other Pokemon on the field, selected by the trainer."


class AllOpponents(Target):
    def __init__(self):
        self.name = "All Opponents"
        self.description = "All opposing Pokemon."


class EntireField(Target):
    def __init__(self):
        self.name = "Entire Field"
        self.description = "The entire field.  Affects all Pokemon."


class UserAndAllies(Target):
    def __init__(self):
        self.name = "User And Allies"
        self.description = "The user and its allies."


class AllPokemon(Target):
    def __init__(self):
        self.name = "All Pokemon"
        self.description = "Every Pokemon on the field."


class AllAllies(Target):
    def __init__(self):
        self.name = "All Allies"
        self.description = "All of the user's allies."


class FaintingPokemon(Target):
    def __init__(self):
        self.name = "Fainting Pokemon"
        self.description = ""


