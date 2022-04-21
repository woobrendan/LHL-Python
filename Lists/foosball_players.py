import math
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
mid = math.ceil(len(foosballers) / 2)

# Get the 5 middle players
mid_five = foosballers[(mid-3):(mid+2)]
