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
        if len(self._dice) == 0:
            self.validation_errors.append('There are no valid dice present')
            return False
        for die in self._dice:
            if type(die).__name__ != 'StandardDie':
                self.validation_errors.append('One or more die are not standard')
                return False
        self.validation_errors = []
        return True

    def validate_dice_present(self):
        pass

    def validate_valid_dice(self):
        pass
