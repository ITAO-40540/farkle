import hashlib


class Game:

    # player is an argument you can use with Game() >> Game(players=...)
    # the input is stored in an instance variable (called an attribute)
    def __init__(self, players = []):
        self._players = players
        self._current_player = players[0]

        self.code = str(hashlib.md5())[-6:-1]

    def players(self):
        return self._players

    # a function that needs to be completed
    def next_player(self):
        if self._current_player == self._players[-1]:
            self._current_player = self._players[0]
        else:
            current_index = self._players.index(self._current_player)
            self._current_player = self._players[current_index + 1]

    def current_player(self):
        return self._current_player
