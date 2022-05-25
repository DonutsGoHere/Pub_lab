class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
    
    def increase_till(self, amount):
        self.till += amount

    def add_drink(self, drink_name):
        self.drinks.append(drink_name)
    
    def sell_a_drink(self, drink, customer):
        self.till += drink.price
        customer.buy_a_drink(drink.price)