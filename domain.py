import random

class Player:

    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def age(self):
        return self._age

    def full_name(self):
        return self.first_name

class Game:

    def __init__(self, players = []):
        self._players = players

    def next_player(self):
        pass

    def current_player(self):
        pass


class ChanceEngine:

    def __init__(self, values=[]):
        self._values = values

    def random_value(self):
        num_of_values = len(self._values)
        selected_index = random.randint(0, num_of_values - 1)
        return self._values[selected_index]

class Dice(ChanceEngine):

    def roll(self):
        print("roll()")
        return self.random_value()

class Coin(ChanceEngine):

    def __init__(self):
        self._values = ['Heads', 'Tails']

    def flip(self):
        return self.random_value()

class StandardDice(Dice):

    def __init__(self):
        self._values = range(1,7)