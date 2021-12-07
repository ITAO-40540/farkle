import pytest
from models.player import Player


class TestGame:

    def test_player_name_is_capitalized(self):
        me = Player('jonathan')
        assert me.first_name == 'Jonathan'
