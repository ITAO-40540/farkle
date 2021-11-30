class Roll:

    def __init__(self, dice):
        self._dice = dice

    def roll(self):
        for die in self._dice:
            die.roll()

    def print(self):
        str = ""
        for die in self._dice:
            str = str + f"{die.value()}"
        return str

