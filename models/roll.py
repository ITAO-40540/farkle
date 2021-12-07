class Roll:

    def __init__(self, dice):
        self._dice = dice
        self.validation_errors = []

    def roll(self):
        for die in self._dice:
            die.roll()

    def print(self):
        str = ""
        for die in self._dice:
            str = str + f"{die.value()}"
        return str

    def is_valid(self):
        for die in self._dice:
            if type(die) != 'StandardDie':
                self.validation_errors << 'One or more die are not standard'
                return False
            self.validation_errors = []
            return True

