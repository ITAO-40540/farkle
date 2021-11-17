import hashlib


class GameInitiationError(Exception):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, message):
        self.message = message

class Game:
    # player is an argument you can use with Game() >> Game(players=...)
    # the input is stored in an instance variable (called an attribute)
    def __init__(self, players):
        if len(players) == 1:
            raise GameInitiationError("Games must include 2 or more players.")

        self._players = players
        self._current_player = players[0]
        self.code = str(hashlib.md5())[:6]
        self.round = 1

    def players(self):
        return self._players

    # a function that needs to be completed
    def next_player(self):
        if self._current_player == self._players[-1]:
            self.__increment_round()
            self._current_player = self._players[0]
        else:
            current_index = self._players.index(self._current_player)
            self._current_player = self._players[current_index + 1]

    def current_player(self):
        return self._current_player

    def __increment_round(self):
        self.round += 1
