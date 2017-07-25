import random

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

    return count
