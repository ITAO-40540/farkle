from models.game import Game
from models.player import Player
import os
os.system("clear")

print("#################################################")
print("############## Play Farkle ######################")
print("#################################################")
print("\n\n")

# ask for the number of players and convert to an int
number_of_players = int(input("How many people playing today? "))

# gonna collect some player objects
players = []

# Ask once for each player, their name and then create a player and add to list
for i in range(number_of_players):
    player_name = input(f"What is player{i + 1}'s name? ")
    players.append(Player(player_name))

# create game from list of players
game = Game(players)

# The game object know everything we need for managing players
print(game)

print("playing a game of Farkle with the following players:")

for player in game.players():
    print(f"-- {player.first_name}")

print(f"current player is {game.current_player().first_name}")