import math
from xxlimited import foo
foosballers = [
    "Mia",
    "Retta",
    "Augustine",
    "Jin",
    "Waylon",
    "Alphonso",
    "Sage",
    "Hubert",
    "Raymon",
    "Rebecca",
    "Monty",
    "Glen",
    "Christi",
    "Patrice",
    "Craig",
    "Dexter",
    "Wally",
    "Ian",
    "Pat"
]

# Get median player


def get_mid():
    return math.ceil(len(foosballers) / 2)


mid = get_mid()
# Get the 5 middle players
mid_five = foosballers[(mid-3):(mid+2)]
# print(mid_five)

# Add fake player called avg player in the middle
foosballers.insert(mid, "Average Player")
# print(foosballers)

# find avg player and put to uppercase .upper()
# print(foosballers[mid].upper())

# add five players to end of list
# append = push
new_players = ["Brendan", "Fred", "Parco", "David", "Chan"]
for player in new_players:
    foosballers.append(player)

# fix where average player is, so they in mid
avg_player = foosballers.index("Average Player")
del foosballers[avg_player]
new_mid = get_mid()
foosballers.insert(new_mid, "Average Player".upper())
# print(foosballers)

# insert Lacy +1 of Hubert
hubert = foosballers.index("Hubert")
foosballers.insert(hubert + 1, "Lacy")
# omar -1 of rebecca
# otto 8th best
# chauncy 10 spots from bottom

print(foosballers)
