from models.dice import ChanceEngine
class Coin(ChanceEngine):

    def __init__(self):
        self._values = ['Heads', 'Tails']

    def flip(self):
        # when you call a method on the class instance, you use `self` just like attributes
        return self.random_value()

