

class PokeballRangeException(Exception):

    def __init__(self, message: str = "The range cannot has different length than 2"):
        self.message = message
        super().__init__(self.message)


class DefineRangeFirst(Exception):

    def __init__(self, message: str = "Please define first the range_between property"):
        self.message = message
        super().__init__(self.message)
