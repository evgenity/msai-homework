class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Liquid(Product):
    pass


class Snack(Product):
    pass


class ProductFactory:
    @staticmethod
    def create_product(name):
        price_dict = {
            'CocaCola': 135,
            'Sprite': 120,
            'Alenka': 60,
            'RitterSport': 120,
            'Snickers': 70,
            'Mars': 60,
        }

        if name in ['CocaCola', 'Sprite']:
            return Liquid(name, price_dict.get(name))
        elif name in ['Alenka', 'RitterSport', 'Snickers', 'Mars']:
            return Snack(name, price_dict.get(name))
        else:
            raise NotImplemented


class VendingMachine:
    def __init__(self):
        # which items are presented on which shelves
        self._items = []
        # how much money inside machine to give change
        self._cash = []
        # which purchases users made
        self._purchases_history = []

    def add_item(self, item):
        self._items.append(item)

    def add_cash(self, cash):
        self._cash = cash

    @property
    def items(self):
        return self._items

    def get_cash_amount(self):
        return sum([k*v for k, v in self._cash.items()])

    def __str__(self):
        return f'Items: {self._items} | Cash: {self._cash} | Total: {self.get_cash_amount()}'

    def __gt__(self, other):
        return self.get_cash_amount() > other.get_cash_amount()


items_a = {'Alenka': 2, 'RitterSport': 1, 'Sprite': 1}
cash_left_a = {10: 100, 5: 100, 1: 99}
A = VendingMachine()
for k, v in items_a.items():
    for _ in range(v):
        A.add_item(ProductFactory.create_product(k))
A.add_cash(cash_left_a)


print(A)
