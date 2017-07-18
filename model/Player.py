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

    def diceThrow(self):
        n = Player.getNumbers(self)
        count = 1
        while count < 3 and n[0] == n[1]:
            count += 1
            n = Player.getNumbers(self)
            print(count)
            if count == 3:
                self.move_to_jail()

    def getNumbers(self):
        d1 = random.sample(range(1, 4), 1)
        d2 = random.sample(range(1, 4), 1)
        print(d1, ",", d2)
        self.move(d1 + d2)
        return d1, d2

    def move(self, number):
        self.position = (self.position + number) % FIELDS_SIZE

    def move_to_jail(self):
        self.position = 5
        self.in_prison = 3
