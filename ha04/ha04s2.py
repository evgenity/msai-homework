class VendingMachine:
    def __init__(self, items, cash):
        # which items are presented on which shelves
        self._items = items
        # how much money inside machine to give change
        self._cash = cash
        # which purchases users made
        self._purchases_history = []

    @property
    def items(self):
        return self._items

    def get_cash_amount(self):
        return sum([k*v for k, v in self._cash.items()])

    def __str__(self):
        return f'Items: {self._items} | Cash: {self._cash} | Total: {self.get_cash_amount()}'

    def __gt__(self, other):
        return self.get_cash_amount() > other.get_cash_amount()

    def __sub__(self, other):
        union_keys = set(self._items.keys()).union(other.items.keys())
        diff = {}
        for k in union_keys:
            diff[k] = max(0, self._items.get(k, 0) - other.items.get(k, 0))
        return diff

    def __or__(self, other):
        union_keys = set(self._items.keys()).union(other.items.keys())
        union = {}
        for k in union_keys:
            union[k] = self._items.get(k, 0) + other.items.get(k, 0)
        return union
        return self._items

    def __and__(self, other):
        union_keys = set(self._items.keys()).union(other.items.keys())
        intersection = {}
        for k in union_keys:
            intersection_key = min(self._items.get(k, 0), other.items.get(k, 0))
            if intersection_key > 0:
                intersection[k] = intersection_key
        return intersection
        return self._items

items_a = {'Alenka': 2, 'RitterSport': 4, 'Snickers': 4}
cash_left_a = {10: 100, 5: 100, 1: 99}
A = VendingMachine(items_a, cash_left_a)

items_b = {'Alenka': 3, 'RitterSport': 5, 'Snickers': 0, 'Mars': 0}
cash_left_b = {10: 100, 5: 100, 1: 100}
B = VendingMachine(items_b, cash_left_b)

print(A)
print(B)
print(A < B)
print(A - B)
print(A & B)
print(A | B)
