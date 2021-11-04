# random is used in ChanceEnging
import random


class Player:
    # __init__() gets executed when Player() is called
    # not necessary to include but very useful in most cases
    def __init__(self, first_name, age):
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

    # a function that needs to be completed
    def next_player(self):
        # `pass` allows you to have an empty execution block
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


class ScoringSet:
    def __init__(self, dice):
        self._dice = dice
        self._dice_as_integers = []

    def points(self):
        self.dice_to_integers()
        value_counts = self.value_counts(self._dice_as_integers)

        if self._dice_as_integers == [1, 2, 3, 4, 5, 6]:
            return 3000
        elif len(value_counts.keys()) == 3 and list(value_counts.values()) == [2, 2, 2]:
            return 1500
        else:
            return self.extract_points(value_counts)

    def len(self):
        return len(self._dice)

    def extract_points(self, value_counts):
        point_total = 0

        try:
            index_of_threes = list(value_counts.values()).index(3)
            value_with_threes = list(value_counts.keys())[index_of_threes]
            value_counts.pop(value_with_threes)
            point_total += self.points_from_threes(value_with_threes)
        except:
            index_of_threes = None
        try:
            index_of_fours = list(value_counts.values()).index(4)
            value_with_fours = list(value_counts.keys())[index_of_fours]
            value_counts.pop(value_with_fours)
            point_total += self.points_from_fours(value_with_fours)
        except:
            # raise
            index_of_fours = None

        point_total += self.points_from_singles(value_counts)

        return point_total

    def points_from_threes(self, value):
        if value == 1:
            return 1000
        else:
            return value * 100

    def points_from_fours(self, value):
        total_points = self.points_from_threes(value)
        total_points += self.points_from_singles({value: 1})
        return total_points

    def points_from_singles(self, value_counts):
        point_total = 0
        for die_val in value_counts.keys():
            die_count = value_counts[die_val]
            for v in range(die_count):
                if die_val == 1:
                    point_total += 100
                elif die_val == 5:
                    point_total += 50

        return point_total

    def value_counts(self, dice_values):
        value_counts = {}
        for i in dice_values:
            if i in value_counts:
                value_counts[i] += 1
            else:
                value_counts[i] = 1
        return value_counts

    def extract_points_from_threes(self, dice_values):
        if dice_values == [1, 1, 1]:
            return 1000
        elif dice_values == [5, 5, 5]:
            return 500
        elif dice_values == [4, 4, 4]:
            return 400
        elif dice_values == [3, 3, 3]:
            return 300
        elif dice_values == [2, 2, 2]:
            return 200
        else:
            return 0

    def dice_to_integers(self):
        self._dice_as_integers = []
        for die in self._dice:
            self._dice_as_integers.append(int(die.value()))
        self._dice_as_integers.sort()
