# import everything from the file domain.py
from domain import *
import os

os.system("clear")

# this is how you create objects from a class file
player = Player("jonathan", 23)
player2 = Player("sebastian", 4)

# create a game and pass in a list of players
game = Game([player, player2])

print(f"{player.first_name} is {player.age()} years old")
print(game)

dice = StandardDice()
coin = Coin()

for i in range(10):
    # loop 10 times, and print the result of the dice.roll() method
    print(dice.roll())