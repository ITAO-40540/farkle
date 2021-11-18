from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from db.base import *
import hashlib
# player is an argument you can use with Game() >> Game(players=...)


class GameInitiationError(Exception):
    def __init__(self, message):
        self.message = message


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    code = Column(String)
    round = Column(Integer, default=1)

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
