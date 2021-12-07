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
        print('===>> run validations')
        self.validation_errors = []

        # run validations
        self.validate_dice_present()
        self.validate_enough_dice()
        self.validate_valid_dice()

        #if any errors, not valid

        if len(self.validation_errors):
            return False
        else:
            return True

    def validate_dice_present(self):
        if len(self._dice) == 0:
            self.validation_errors.append('There are no valid dice present')

    def validate_valid_dice(self):
        for die in self._dice:
            if type(die).__name__ != 'StandardDie':
                self.validation_errors.append('One or more die are not standard')

    def validate_enough_dice(self):
        if len(self._dice) < 2:
            self.validation_errors.append('Less than 2 dice present')
