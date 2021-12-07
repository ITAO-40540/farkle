import pytest
from models.player import Player


class TestGame:

    def test_player_name_is_capitalized(self):
        me = Player('jonathan')
        assert me.first_name == 'Jonathan'

    def test_player_with_multiple_names_is_capitalized(self):
        me = Player('anna beth')
        assert me.first_name == 'Anna Beth'