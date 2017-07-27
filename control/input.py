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

def what_we_do():
    try:
        do = input("Do you want to roll a dice?(y/n) ")
    except:
        do = '0'

    while do not in ['y', 'n']:
        try:
            do = input("Do you want to roll a dice?(y/n) ")
        except:
            do = '0'

    if do == "y":
        return True
    elif do == "n":
        return False

def field_decisions(type): # another argument to know is the city has an owner
    if type == 'Field':
        print("Do nth")
    elif type == 'CityCard':
        return input("Choose one letter: \n ")
    elif type == 'Railway':
        return input("Choose one letter: \n ")
    elif type == 'Chance':
        return input("Choose one letter: \n ")
    elif type == 'Jail':
        return input("Choose one letter: \n ")