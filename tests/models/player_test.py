import pytest
from models.player import Player


class TestPlayer:

    def test_player_name_is_capitalized(self):
        me = Player('jonathan')
        assert me.first_name == 'Jonathan'

    # need to make sure this happens with important people with many names
    def test_player_with_multiple_names_is_capitalized(self):
        me = Player('anna beth')
        assert me.first_name == 'Anna Beth'