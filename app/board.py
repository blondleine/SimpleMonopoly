import random
import sys
from model.Field import Field, CityCard, Chance, Railway, Jail
from control.input import player_decision, what_we_do, field_decisions, auction
from model.Player import Player
from gui.StartFrame import StartFrame
from gui.GameFrame import GameFrame, QApplication

TOKENS = ["Automobile", "Top Hat", "Penguin", "T-Rex", "Cat"]


def run():
    # game frame
    app = QApplication(sys.argv)
    game_frame = GameFrame()
    sys.exit(app.exec_())
    fields = get_fields()
    chance_cards = get_chance_cards()
    # start frame
    start_frame = StartFrame(TOKENS)
    players = create_player(start_frame.players_nicks, start_frame.players_tokens)
    start_game(players, fields, chance_cards)


def get_fields():
    objects = []
    fields = {
        '1': Field("START", 1),
        '2': CityCard("AA", 2, 50, 15, "RED"),
        '3': CityCard("AB", 3, 50, 15, "RED"),
        '4': Chance("CHANCE", 4),
        '5': Field("JAIL", 5),
        '6': Chance("COMMUNITY CHEST", 6),
        '7': CityCard("BA", 7, 90, 20, "GREEN"),
        '8': CityCard("BB", 8, 110, 22, "GREEN"),
        '9': Field("PARKING", 9),
        '10': Railway("AAA", 10, 8, 6),
        '11': CityCard("CA", 11, 130, 26, "BLUE"),
        '12': CityCard("CB", 12, 150, 28, "BLUE"),
        '13': Jail("GO TO JAIL", 13, 0, 0, True),
        '14': CityCard("DA", 14, 170, 32, "YELLOW"),
        '15': CityCard("DB", 15, 190, 30, "YELLOW"),
        '16': Chance("CHANCE", 16)
    }
    for field in fields.items():
        objects.append(field[1])
    return objects


def get_chance_cards():
    cards = {
        '1': (-200),
        '2': 200,
        '3': (-100),
        '4': 100,
        '5': (-150),
        '6': 150,
        '7': (-50),
        '8': 50
    }
    return cards


def create_player(nicks, tokens):

    players = []

    for i in range(len(nicks)):
        players.append(Player(nicks[i], tokens[i]))

    return players


def start_game(players, fields, chance_cards):
    count = 0
    id = 0
    num_of_players = len(players)
    while num_of_players > 1 and num_of_players > id:
        print("*********************************** " + players[id].nick + "'s turn ***********************************")
        if what_we_do():  # temporarily
            turn(count, id, players, fields, chance_cards)
            id += 1
        else:
            num_of_players = 1


def turn(count, i, players, fields, chance_cards):
    do = player_decision()  # ask what to do

    if do == 'd':
        doublet = True

        while doublet:
            doublet, count = players[i].player_move(count)
            print("You are standing on " + fields[players[i].position - 1].name + "\n *** \n")
            if fields[players[i].position - 1].owner == "bank":
                do_it = field_decisions(type(fields[players[i].position - 1]).__name__, False)
            else:
                do_it = field_decisions(type(fields[players[i].position - 1]).__name__, True)
            if do_it == 'a':
                player, offer = auction(fields[players[i].position - 1].price, players)
                buy_it(player, fields[players[i].position - 1], offer)

            elif do_it == 'b':
                buy_it(players[i], fields[players[i].position - 1], fields[players[i].position - 1].price)

            elif do_it == 'p':
                pay_rent(players, i, fields, players[i].position - 1)

            elif do_it == 'r':
                amount = read_it(chance_cards)
                if amount > 0:
                    print("You get " + str(amount))
                elif amount < 0:
                    print("You pay " + str(-amount))
                elif amount == 0:
                    pass
                print(players[i].nick + " had " + str(players[i].money))
                
                players[i].money = players[i].money + amount
                
                print("Now " + players[i].nick + " has " + str(players[i].money))

    elif do == 'h':
        players[i].buy_house()  # parameter from control package
        players[i].dice_throw()

    elif do == 'm':
        players[i].mortgage()  # parameter from control package
        players[i].dice_throw()


def buy_it(player, card, price):
    card.owner = player.nick
    player.money = player.money - price
    print(card.owner + "'ve bought it for " + str(price) + "\n" + player.nick + " has " + str(player.money))


def pay_rent(players, i, fields, position):
    owner = list(filter(lambda x: x.nick == fields[position].owner, players))[0]
    rent = fields[position].rent  # check which value of the rent (owner of all district) ->>filter and maps

    print(players[i].nick + " has " + str(players[i].money) + "\n")
    print(fields[position].owner + " (" + owner.nick + ") " + " has " + str(owner.money) + "\n")
    players[i].money = players[i].money - rent
    owner.money += rent
    # filter the player by nick (it is in field.owner) and add him money
    print(players[i].nick + "'ve paid " + str(rent) + " for " + fields[position].owner + "\n")
    print(players[i].nick + " has " + str(players[i].money) + "\n")
    print(fields[position].owner + " (" + owner.nick + ") " + " has " + str(owner.money) + "\n")


def read_it(cards):
    x = str(random.sample(range(1, len(cards)), 1)[0])

    return cards[x]
run()
