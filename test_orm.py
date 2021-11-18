from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import configure_mappers
from db.base import *
import os

from models.game import Game
from models.player import Player
os.system('clear')

session = sessionmaker()

# setup db in folder 'db' and file name of farkle.sqlite
engine = create_engine(f"sqlite:///db/farkle.sqlite")
session.configure(bind=engine)

# create all the tables
# delete db file to regenerate
Base.metadata.create_all(engine)

# you can use this variable to add and commit your changes
ses = session()

p1,p2 = Player('Jack'), Player('Jill')
game = Game([p1,p2])

ses.add(game)
ses.commit()

all_games = ses.query(Game).all()
print(f"there are {len(all_games)} game(s)")