import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Daffy Duck", 20.00, 19)

    def test_customer_has_name(self):
        self.assertEqual("Daffy Duck", self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(20.00, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(19, self.customer.age)

    def test_customer_has_id(self):
        self.assertEqual(True, self.customer.is_over_18())