from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.base import *

from models.game import Game
from models.player import Player
from models.dice import StandardDie
from models.roll import Roll
import os
os.system("clear")

session = sessionmaker()

# setup db in folder 'db' and file name of farkle.sqlite
engine = create_engine(f"sqlite:///db/farkle.sqlite")
session.configure(bind=engine)

# create all the tables
# delete db file to regenerate
Base.metadata.create_all(engine)

# you can use this variable to add and commit your changes
ses = session()

all_games = ses.query(Game).all()

print("Here are the games...")

for game in all_games:
    print(f"-- [{game.id}] {game.code}")

game_id = int(input("Which game (by id) do you want to view? "))

game = ses.query(Game).get(game_id)

print(f"Cool. You have info on game with code of {game.code}")
print("here are the players")

for player in game.players:
    print(f"-- {player.first_name}")
