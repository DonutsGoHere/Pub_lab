import unittest

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100, [{"Tennants": 3.80}, {"Whiskey": 5.00}, {"House Red": 2.75}, {"White Wine Spritzer": 1.95}])
        
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_has_till(self):
        # expected_value = 100
        # actual_value = self.pub.till
        # self.assertEqual(expected_value, actual_value)
        self.assertEqual(100, self.pub.till)
    
    def test_increase_till(self):
        self.pub.increase_till(50)
        self.assertEqual(150, self.pub.till)
    
    def test_pub_has_drinks(self):
        self.assertEqual(4, len(self.pub.drinks))

    def test_add_drink_to_pub(self):
        self.pub.add_drink("Vanilla Maitai")
        self.assertEqual(5, len(self.pub.drinks))

    def test_sell_a_drink(self):
        customer = Customer("Daffy Duck", 20.00)
        beer = Drink("Tennants", 3.80)
        self.pub.sell_a_drink(beer, customer)
        self.assertEqual(16.20, customer.wallet)
        self.assertEqual(103.80, self.pub.till)

