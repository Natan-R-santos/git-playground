import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Natan",100)

    def test_deposit_valid(self):
        result = self.account.deposit(100)
        self.assertEqual(result,"deposit with sucess!")

    def test_deposit_value_zero(self):
        deposit= 0
        result = self.account.deposit(deposit)
        self.assertEqual(result,"value invalid, just number positive")
        self.assertEqual(self.account.amount,100)

    def test_deposit_value_negative(self):
        result = self.account.deposit(-100)
        self.assertEqual(result,"value invalid, just number positive")
        self.assertEqual(self.account.amount,100)

    def test_update_new_name(self):
        new_name= "dev natan"
        result = self.account.update_new_name(new_name)
        self.assertEqual(self.account.name, "Dev Natan")
        self.assertEqual(result, "new name this account is: Dev Natan")
