from domain import *
import os

os.system("clear")

player = Player("jonathan", 23)
player2 = Player("sebastian", 4)

game = Game([player, player2])

print(f"{player.first_name} is {player.age()} years old")
print(game)

dice = StandardDice()
coin = Coin()

for i in range(10):
    print(dice.roll())
