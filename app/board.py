from model.Field import Field, CityCard, Chance, Railway, Jail
from control.input import getPlayers, createPlayers

def run():
    fields = getFields()
    players = getPlayers()
    print(players)

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

run()