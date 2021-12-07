# random is used in ChanceEnging
import random


class ChanceEngine:

    def __init__(self, values=[], initial_value=None):
        self._values = values

    def random_value(self):
        num_of_values = len(self._values)
        selected_index = random.randint(0, num_of_values - 1)
        return self._values[selected_index]


# this is the syntax for using inheritance
# Dice will inherit the attributes and methods of ChanceEnging
class Die(ChanceEngine):
    def __init__(self, values, initial_value=None):
        super().__init__(values)
        if initial_value:
            self._current_value = initial_value
        else:
            self.roll()

    def roll(self):
        self._current_value = self.random_value()

    def current_value(self):
        return self._current_value

class StandardDie(Die):

    def __init__(self, initial_value=None):
        self._values = range(1,7)
        super().__init__(self._values, initial_value)
