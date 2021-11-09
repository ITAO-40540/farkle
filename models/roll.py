class Roll:

    def __init__(self, dice):
        self._dice = dice

    def roll(self):
        for die in self._dice:
            die.roll()
