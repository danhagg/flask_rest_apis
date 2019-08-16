class LotteryPlayer:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer(name="dan", numbers=(2,4,6))
player_two = LotteryPlayer(name="bob", numbers=(1,2,3))
# print(player_one.name)
# print(neg(player_one.total()))


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {'name': name, 'price': price}
        return self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        return sum([item['price'] for item in self.items])

    @classmethod
    def franchise(cls, store):
        return f'{store.name} - franchise'
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return f'{store.name}, total stock price: {store.stock_price()}'


store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

print(Store.franchise(store))
print(Store.franchise(store2))

print(Store.store_details(store))
print(Store.store_details(store2))