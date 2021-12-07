import pytest
from models.roll import Roll
from models.dice import StandardDie
from models.coin import Coin

class TestRoll:
    def test_validate_dice(self):
        roll = Roll()
        dice1 = StandardDie()
        dice2 = Coin()

        assert not roll.is_valid()
