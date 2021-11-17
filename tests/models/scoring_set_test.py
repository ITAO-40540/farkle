import pytest
from models.scoring_set import *
from models.dice import StandardDie

class TestScoringSet:

    def test_straight(self):
        dice = []

        for i in range(1,7):
            dice.append(StandardDie(i))

        sset = ScoringSet(dice)
        assert sset.points() == 3000