import pytest
from models.roll import Roll
from models.dice import StandardDie
from models.coin import Coin


class TestRoll:

    def test_invalid_dice(self):
        dice1 = StandardDie()
        dice2 = Coin()
        roll = Roll([dice1, dice2])
        assert not roll.is_valid()
        assert roll.validation_errors[0] == 'One or more die are not standard'

    def test_valid_dice(self):
        dice1 = StandardDie()
        dice2 = StandardDie()
        roll = Roll([dice1, dice2])
        assert roll.is_valid()
        assert len(roll.validation_errors) == 0

    def test_empty_dice_is_invalid(self):