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

print("#################################################")
print("############## Play Farkle ######################")
print("#################################################")
print("\n\n")

number_of_players = int(input("How many players are going to join the game? "))
player_list = []

for i in range(number_of_players):
    name = input("What is the players name? ")
    p = Player(first_name=name)
    player_list.append(p)

print(f"adding {len(player_list)} players to a game...")
game = Game(players=player_list)

ses.add(game)
ses.commit()

dice = []
for i in range(6):
    dice.append(StandardDie())


print("Game On!")

game_active = True

while game_active:

    print(f"Player Up! {game.current_player().first_name}'s turn.")

    Roll(dice).roll()


    game_active = False