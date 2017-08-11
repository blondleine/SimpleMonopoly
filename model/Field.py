DISTRICT = {
    'RED': 50,
    'BLUE': 100,
    'GREEN': 150,
    'PINK': 200,
}


class Field(object):

    def __init__(self, name, number, price=0, rent=0, owner="bank"):
        self.name = name
        self.number = number
        self.rent = rent
        self.price = price
        self.owner = owner


class CityCard(Field):

    def __init__(self, name, number, price=0, rent=0, district="", owner="bank"):
        super(CityCard, self).__init__(name, number, price, rent)
        self.house_price = DISTRICT.get(district, 0)
        self.owner = owner


class Railway(Field):
    def __init__(self, name, number, price=0, rent=0, owner="bank"):
        super(Railway, self).__init__(name, number, price, rent)
        self.owner = owner


class Chance(Field):
    def __init__(self, name, number, price=0, rent=0, owner="bank"):
        super(Chance, self).__init__(name, number, price, rent)
        self.owner = owner


class Jail(Field):
    def __init__(self, name, number, price=0, rent=0, is_in=False, owner="bank"):
        super(Jail, self).__init__(name, number, price, rent)
        self.is_in = is_in
        self.owner = owner
