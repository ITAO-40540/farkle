# import everything from the file domain.py
from domain import *
import os
os.system("clear")

scenarios = {
    500: [5, 5, 5],
    1000: [1, 1, 1],
    3000: [1, 2, 3, 4, 5, 6],
    400: [4, 4, 4],
    200: [1, 5, 5]
}
scoring_sets = []

for k in scenarios.keys():
    dice = []
    for i in scenarios[k]:
        dice.append(StandardDie(i))
    scoring_sets.append(ScoringSet(dice))

for i in range(len(scoring_sets)):
    print(scoring_sets[i].points(), ' == ', list(scenarios.keys())[i])

