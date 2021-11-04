# random is used in ChanceEnging
import random


class Player:
    # __init__() gets executed when Player() is called
    # not necessary to include but very useful in most cases
    def __init__(self, first_name, age=None):
        # self is a hook into the object created. It's how you add attributes
        self.first_name = first_name
        # the `_` signifies that the attribute should be treated as private
        self._age = age

    # these are functions that are hooked into the object but their strucure is a plain old function
    def age(self):
        return self._age

    def full_name(self):
        return self.first_name


class Game:
    # player is an argument you can use with Game() >> Game(players=...)
    # the input is stored in an instance variable (called an attribute)
    def __init__(self, players = []):
        self._players = players
        self._current_player = players[0]

    def players(self):
        return self._players

    # a function that needs to be completed
    def next_player(self):
        # `pass` allows you to have an empty execution block
        pass

    def current_player(self):
        return self._current_player


class ChanceEngine:

    def __init__(self, values=[]):
        self._values = values

    def random_value(self):
        num_of_values = len(self._values)
        selected_index = random.randint(0, num_of_values - 1)
        return self._values[selected_index]

# this is the syntax for using inheritance
# Dice will inherit the attributes and methods of ChanceEnging
class Dice(ChanceEngine):

    def roll(self):
        print("roll()")
        return self.random_value()


class Coin(ChanceEngine):

    def __init__(self):
        self._values = ['Heads', 'Tails']

    def flip(self):
        # when you call a method on the class instance, you use `self` just like attributes
        return self.random_value()


class StandardDice(Dice):

    def __init__(self):
        self._values = range(1,7)