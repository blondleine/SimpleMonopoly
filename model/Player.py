import random

FIELDS_SIZE = 16

class Player(object):
    MONEY = 1500
    in_prison = 0

    def __init__(self, nick, token):
        self.nick = nick
        self.token = token
        self.money = self.MONEY
        self.position = 0

    def dice_roll(self):
        i, j = self.getNumbers()
        return i, j

    def getNumbers(self):
        d1 = random.sample(range(1, 4), 1)[0]
        d2 = random.sample(range(1, 4), 1)[0]
        return d1, d2

    def move(self, number):
        self.position = (self.position + number) % FIELDS_SIZE

    def move_to_jail(self):
        self.position = 5
        self.in_prison = 3

    def buy_house(self):
        print("Write the number of houses to buy:")

    def mortgage(self):
        print("write the name of property to mortgage:")

    def bancruptcy(self):

        if(self.money == 0):
            return True
        else:
            return False

    def is_doublet(self, i, j, count):
        while count < 3 and i == j:
            print("You've got doublet")
            self.player_move(count)

        if count == 3:
            print("Go to jail!")
            self.move_to_jail(    )

    def player_move(self, count):
        x, y = self.dice_roll()
        count += 1
        # m = x[0] + y[0]
        self.move(x + y)
        print("Yours dices show: " + str(x) + " and " + str(y))
#        what field?
        self.is_doublet(x, y, count)

        print(self.token + "'ve moved")

        return self.position