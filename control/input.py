import random

TOKENS = ["Automobile", "Top Hat", "Penguin", "T-Rex", "Cat"]

def getPlayers():
    count = int(input("Enter the number of players (2 to 5):"))

    if count in list(range(2, 6)):
        return createPlayers(count)
    else:
        getPlayers()

def createPlayers(count):
    tokens = random.sample(range(len(TOKENS)), count)  # choose random token
    players = []

    for i in range(count):

        players.append(TOKENS[tokens[i]])

    print(players)
    return players