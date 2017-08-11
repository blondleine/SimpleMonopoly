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

    def move(self, number):
        self.position = (self.position + number) % FIELDS_SIZE

    def move_to_jail(self):
        self.position = 5
        self.in_prison = 3

    def bancruptcy(self):

        if self.money == 0:
            return True
        else:
            return False

    def is_doublet(self, i, j, count):
        if count < 3 and i == j:
            print("It was doublet \n")
            return True

        elif count == 3 and i == j:
            print("Go to jail!")
            self.move_to_jail()
            return False

        else:
            return False

    def player_move(self, count):
        x, y = dice_throw()
        count += 1
        print("____________" + self.nick + " -> "
              + str(count) + " dice throw _________________________________________________")
        print("Yours dices show: " + str(x) + " and " + str(y))
        self.move(x + y)
        print(self.token + "'ve moved")
        # what field?
        doublet = self.is_doublet(x, y, count)

        return doublet, count


def buy_house():
    print("NOT DONE YET")


def get_numbers():
    d1 = random.sample(range(1, 6), 1)[0]
    d2 = random.sample(range(1, 6), 1)[0]

    return d1, d2


def dice_throw():
    i, j = get_numbers()
    return i, j
