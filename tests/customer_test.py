import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Daffy Duck", 20.00)

    def test_customer_has_name(self):
        self.assertEqual("Daffy Duck", self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(20.00, self.customer.wallet)

    # def test_buy_a_drink(self):
    #     self.customer.buy_a_drink(3.80)
    #     self.assertEqual(16.20, self.customer.wallet)
    #     self.assertEqual(103.80, self.pub.till)