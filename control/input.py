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


def player_decision():
    try:
        do = str(input("Choose one letter: \n dice throw - d \n buy house/s - h \n mortgage property - m: \n"))
    except:
        do = '0'

    while do not in ['d', 'h', 'm']:
        try:
            do = str(input("Choose one letter: \n dice throw - d \n buy house/s - h \n mortgage property - m: \n"))
        except:
            do = '0'

    return do

