import unittest
from main import something

class TestSomething(unittest.TestCase):
    def test_returns_dev_prefix_for_natan(self):
        args_test = "Natan" 
        result = something(args_test)
        self.assertEqual("Hello Dev Natan", result)
