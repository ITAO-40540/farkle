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
        roll = Roll([])
        assert not roll.is_valid()
        assert roll.validation_errors[0] == 'There are no valid dice present'

    def test_validate_more_than_one_die(self):
        roll = Roll([StandardDie])
        assert not roll.is_valid()
        assert roll.validation_errors[0] == 'Less than 2 dice present'

    def test_multiple_validation_errors(self):
        roll = Roll([Coin])
        assert not roll.is_valid()
        assert len(roll.validation_errors) == 2