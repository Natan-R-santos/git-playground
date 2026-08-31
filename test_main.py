import unittest
from main import soma, something
from bank import BankAccount

class TestSoma(unittest.TestCase):
    def test_soma_num_positive(self):
        num1 = 100
        num2 = 100
        result = soma(num1,num2)
        self.assertEqual(result,200)

    def test_soma_num_negativo(self):
        num1 = -1
        num2 = 10
        result = soma(num1,num2)
        self.assertEqual(result,0)

class TestSomething(unittest.TestCase):
    def test_something_name(self):
        name = "Natan"
        result = something(name)
        self.assertEqual(result,"Hello Dev: Natan, welcome")

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

    
if __name__ == "__main__":
    unittest.main()