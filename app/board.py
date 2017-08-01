import random
from model.Field import Field, CityCard, Chance, Railway, Jail
from control.input import getPlayers, player_decision, what_we_do, field_decisions, auction
from model.Player import Player

TOKENS = ["Automobile", "Top Hat", "Penguin", "T-Rex", "Cat"]

def run():
    fields = getFields()
    chance_cards = get_chance_cards()
    number = getPlayers()
    players = create_player(number)
    chances = create_chances()
    print(chances)

    for i in range(number):
        print(players[i].nick, players[i].token)

    start_game(players, fields, chance_cards)

def getFields():
    objects = []
    fields = {
        '1': Field("START", 1),
        '2': CityCard("AA", 2, 15, 50, "RED"),
        '3': CityCard("AB", 3, 15, 50, "RED"),
        '4': Chance("CHANCE", 4),
        '5': Field("JAIL", 5),
        '6': Chance("COMMUNITY CHEST", 6),
        '7': CityCard("BA", 7, 20, 90, "GREEN"),
        '8': CityCard("BB", 8, 22, 110, "GREEN"),
        '9': Field("PARKING", 9),
        '10': Railway("AAA", 10, 8, 6),
        '11': CityCard("CA", 11, 26, 130, "BLUE"),
        '12': CityCard("CB", 12, 28, 150, "BLUE"),
        '13': Jail("GO TO JAIL", 13, 0, 0, True),
        '14': CityCard("DA", 14, 32, 190, "YELLOW"),
        '15': CityCard("DB", 15, 30, 170, "YELLOW"),
        '16': Chance("INCOME TAX", 16, -200)
    }
    for field in fields.items():
        objects.append(field[1])
    return objects

def get_chance_cards():
    cards = {
        '1': "Pay 200",
        '2': "Get 200",
    }
    return cards
def create_player(number):

    tokens_id = random.sample(range(len(TOKENS)), number)  # choose random token
    players = []

    for i in range(number):
        nick = 'Player' + str(i+1)
        players.append(Player(nick, TOKENS[tokens_id[i]]))

    return players

def create_chances():
    return random.sample(range(-100, 100, 10), 10)

def start_game(players, fields, chance_cards):
    count = 0
    id = 0
    num_of_players = len(players)
    while num_of_players > 1 and id < num_of_players:
        if what_we_do() == True:#temporarily
            # print("******  " + players[id].name +"   ************************************")
            turn(count, id, players, fields,chance_cards)
            id = (id + 1)
        else:
            num_of_players = 1

def turn(count, i, players, fields, chance_cards):
    do = player_decision()  # ask what to do

    if do == 'd':
        doublet, count = players[i].player_move(count)
        print("You are standing on " + fields[players[i].position - 1].name + "\n *** \n")

        if fields[players[i].position - 1].owner == "bank":
            do_it = field_decisions(type(fields[players[i].position - 1]).__name__, False)
        else:
            do_it = field_decisions(type(fields[players[i].position - 1]).__name__, True)
        while doublet == True:
            doublet, count = players[i].player_move(count)
            print("You are standing on " + fields[players[i].position - 1].name + "\n *** \n")
            if fields[players[i].position - 1].owner == "bank":
                do_it = field_decisions(type(fields[players[i].position - 1]).__name__, False)
            else:
                do_it = field_decisions(type(fields[players[i].position - 1]).__name__, True)

        if do_it == 'a':
            player, offer = auction(fields[players[i].position - 1].price, players)
            buy_it(players[i], fields[players[i].position - 1].price / 2)

        elif do_it == 'b':
            buy_it(players[i], fields[players[i].position - 1], fields[players[i].position - 1].price)

        elif do_it == 'p':
            pay_rent(players, i, fields, players[i].position - 1)

        elif do_it == 'r':
            pass

    elif do == 'h':
        players[i].buy_house()
        players[i].dice_roll()

    elif do == 'm':
        players[i].mortgage()
        players[i].dice_roll()

def buy_it(player, card, price):
    card.owner = player.nick
    player.money = player.money - price

def pay_rent(players, i, fields, position):
    rent = fields[position].rent #check which value of the rent (owner of all district) ->>filter and maps
    players[i].money = players[i].money - rent
    #filter the player by nick (it is in field.owner) and add him money

def read_it(chance_cards):
    x = str(random.sample(range(1, len(chance_cards)), 1)[0])
    return chance_cards[x]
run()