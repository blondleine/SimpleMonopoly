def get_players():
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


def player_decision(is_owner):
    if is_owner:
        ask = "Choose one letter: \n dice throw - d \n buy house/s - h \n"
        options = ['d', 'h']
    else:
        ask = "Choose one letter: \n dice throw - d \n"
        options = ['d']
    try:
        do = str(input(ask))
    except:
        do = '0'

    while do not in options:
        try:
            do = str(input(ask))
        except:
            do = '0'

    return do


def field_decisions(type, has_owner):  # another argument to know is the city has an owner
    if type == 'Field':
        print("Do nth")
        do = 0
    elif type == 'CityCard' or type == 'Railway':
        if has_owner:
            try:
                do = input("Choose one letter: \n  pay the rent - p \n")
            except:
                do = 0
            while do not in ['b', 'p']:
                try:
                    do = input("Choose one letter: \n pay the rent - p \n")
                except:
                    do = 0
        elif not has_owner:
            try:
                do = input("Choose one letter: \n buy it - b \n for the auction - a \n")
            except:
                do = 0
            while do not in ['b', 'a']:
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
    return do


def auction(price, players):
    print("Start offer is " + str(price/2))
    users = map(lambda x: x.nick, players)
    try:
        nick = input("Write nick (player who gave final offer)")
    except:
        nick = 0
    while nick not in users:
        try:
            nick = input("Write nick (player who gave final offer)")
        except:
            nick = 0

    try:
        offer = int(input("Write your offer"))
    except:
        offer = 0
    while offer < price/2:
        try:
            offer = int(input("Write your offer"))
        except:
            offer = 0

    return nick, offer
