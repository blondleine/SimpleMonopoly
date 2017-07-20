import random

TOKENS = ["Automobile", "Top Hat", "Penguin", "T-Rex", "Cat"]

def getPlayers():
    try:
        count = int(input("Enter the number of players (2 to 5):"))
    except:
        count = 0

    while count not in list(range(2, 6)):
        try:
            count = int(input("Enter the number of players (2 to 5):"))
        except:
            count = 0

    return createPlayers(count)

def createPlayers(count):
    tokens = random.sample(range(len(TOKENS)), count)  # choose random token
    players = []

    for i in range(count):

        players.append(TOKENS[tokens[i]])

    return players