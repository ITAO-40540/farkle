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
