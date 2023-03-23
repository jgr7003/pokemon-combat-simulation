

class CatchRateException(Exception):

    def __init__(self, message="Range can be a float between 0.00 and 1.00"):
        self.message = message
        super().__init__(self.message)
