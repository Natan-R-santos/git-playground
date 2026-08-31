import unittest

def soma(a,b):
    return a +b

def something(name:str):
    msg = f"Hello Dev: {name}, welcome"
    return msg

class TestSoma(unittest.TestCase):
    def test_soma_num_positive(self):
        num1 = 100
        num2 = 100
        result = soma(num1,num2)
        self.assertEqual(result,200)

    def test_soma_num_negative(self):
        num1 = -1
        num2 = 1
        result = soma(num1,num2)
        self.assertEqual(result,0)

class TestSomething(unittest.TestCase):
    def test_something_name(self):
        name = "Natan"
        result = something(name)
        self.assertEqual(result,"Hello Dev: Natan, welcome")
    
if __name__ == "__main__":
    unittest.main()



