from domain import *
import os
os.system("clear")

print("#################################################")
print("############## Play Farkle ######################")
print("#################################################")
print("\n\n")

number_of_players = int(input("How many people playing today? "))
players = []
for i in range(number_of_players):
    player_name = input(f"What is player{i + 1}'s name? ")
    players.append(Player(player_name))

game = Game(players)

print(game)

print("playing a game of farkle with the following players:")

for player in game.players():
    print(f"-- {player.first_name}")

print(f"current player is {game.current_player().first_name}")