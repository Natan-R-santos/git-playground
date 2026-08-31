import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Natan",100)

    def test_deposit_valid(self):
        result = self.account.deposit(50)
        self.assertEqual(result,150)

    def test_deposit_value_zero(self):
        deposit= 0
        result = self.account.deposit(deposit)
        self.assertEqual(result,"value invalid, just number positive")

    def test_deposit_value_negative(self):
        result = self.account.deposit(-100)
        self.assertEqual(result,"value invalid, just number positive")
        self.assertEqual(self.account.amount,100)