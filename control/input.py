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

def field_decisions(type, has_owner): # another argument to know is the city has an owner
    if type == 'Field':
        print("Do nth")
        do = 0
    elif type == 'CityCard' or type == 'Railway':
        if has_owner == True:
            try:
                do = input("Choose one letter: \n  pay the rent - p \n")
            except:
                do = 0
            while do not in ['b', 'p']:
                try:
                    do = input("Choose one letter: \n pay the rent - p \n")
                except:
                    do = 0
        elif has_owner == False:
            try:
                do = input("Choose one letter: \n buy it - b \n for the auction - a \n")
            except:
                do = 0
            while do not in ['b', 'a ']:
                try:
                    do = input("Choose one letter: \n buy it - b \n for the auction - a \n")
                except:
                    do = 0

    elif type == 'Chance':
        try:
            do = input("Choose one letter: \n read it - r \n")
        except:
            do = 0
        while do not in ['r']:
            try:
                do = input("Choose one letter: \n read it - r \n")
            except:
                do = 0
    return  do

def auction(price, players):
    try:
        nick = input("Write nick (player who gave final offer)")
    except:
        nick = 0
    while nick not in players:
        try:
            nick = input("Write nick (player who gave final offer)")
        except:
            nick = 0

    offer = input("Write your offer")

    return nick, offer