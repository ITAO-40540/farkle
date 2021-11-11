# import everything from the file domain.py
from models.dice import StandardDie
from models.scoring_set import ScoringSet
import os

os.system("clear")

# create a dictionary that encapsulates the rules for aquiring points
# key is the expected points, values are a list of dice that would get those points
scenarios = {
    500: [5, 5, 5],
    1000: [1, 1, 1],
    3000: [1, 2, 3, 4, 5, 6],
    400: [4, 4, 4],
    200: [1, 5, 5]
}
# gonna create a bunch of scoring sets from dictionary above
scoring_sets = []

# loop though all the keys
for k in scenarios.keys():

    dice = []
    for i in scenarios[k]:
        # instantiate the dice objects with the values from the dictionary
        dice.append(StandardDie(i))

    # create a scoring set from dice and append to the list
    scoring_sets.append(ScoringSet(dice))

# once done, loop though all the scoring sets (or the dictionary keys)
# print out the two values and they should match
for i in range(len(scoring_sets)):
    print(scoring_sets[i].points(), ' == ', list(scenarios.keys())[i])

