class Customer:
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness


    def buy_a_drink(self, amount):
        self.wallet -= amount
        
    def is_over_18(self):
        return self.age >= 18
    
