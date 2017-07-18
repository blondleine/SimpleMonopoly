DISTRICT = {
    'RED': 50,
    'BLUE': 100,
    'GREEN': 150,
    'PINK': 200,
}

class Field(object):

    def __init__(self, name, number, price = 0, rent = 0):
        self.name = name
        self.number = number
        self.rent = rent
        self.price = price

class CityCard(Field):

    def __init__(self, name, number, price = 0, rent = 0, district= ""):
        super(CityCard, self).__init__(name, number, price, rent)
        self.house_price = DISTRICT.get(district, 0)


class Railway(Field):
    def __init__(self, name, number, price=0, rent=0):
        super(Railway, self).__init__(name, number, price, rent)


class Chance(Field):
    def __init__(self, name, number, price=0, rent=0):
        super(Chance, self).__init__(name, number,0 ,0)

class Jail(Field):
    def __init__(self, name, number, price=0, rent=0, is_in=False):
        super(Jail, self).__init__(name, number, 0, 0)
        self.is_in = is_in