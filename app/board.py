import random
from model.Field import Field, CityCard, Chance, Railway, Jail
from control.input import getPlayers, player_decision
from model.Player import Player

TOKENS = ["Automobile", "Top Hat", "Penguin", "T-Rex", "Cat"]

def run():
    fields = getFields()
    number = getPlayers()
    players = create_player(number)
    chances = create_chances()

    print(chances)
    for i in range(number):
        print(players[i].nick, players[i].token)

    start_game(players)

def getFields():
    objects = []
    fields = {
        '1': Field("START", 1),
        '2': CityCard("AA", 2, 15, 50, "RED"),
        '3': CityCard("AB", 3, 15, 50, "RED"),
        '4': Chance("CHANCE", 4),
        '5': Field("JAIL", 5),
        '6': Railway("COMMUNITY CHEST", 6),
        '7': CityCard("BA", 7, 20, 90, "GREEN"),
        '8': CityCard("BB", 8, 22, 110, "GREEN"),
        '9': Field("PARKING", 9),
        '10': Railway("AAA", 10, 8, 6),
        '11': CityCard("CA", 11, 26, 130, "BLUE"),
        '12': CityCard("CB", 12, 28, 150, "BLUE"),
        '13': Jail("GO TO JAIL", 13, 0, 0, True),
        '14': CityCard("DB", 14, 32, 190, "YELLOW"),
        '15': CityCard("DA", 15, 30, 170, "YELLOW"),
        '16': Chance("INCOME TAX", 16, -200)
    }
    for field in fields.items():
        objects.append(field[1])
    return objects

def create_player(number):

    tokens_id = random.sample(range(len(TOKENS)), number)  # choose random token
    players = []

    for i in range(number):
        nick = 'Player' + str(i+1)
        players.append(Player(nick, TOKENS[tokens_id[i]]))

    return players

def create_chances():
    return random.sample(range(-100, 100, 10), 10)

def start_game(players):

    do = player_decision() #ask what to do

    i = 0
    if do == 'd':
        players[i].dice_throw()
        players[i].move()
    elif do == 'h':
        players[i].buy_house()

    else:
        players[i].mortgage()

run()