class BankAccount():
    def __init__(self,name:str,amount:int):
        self.name = name
        self.amount = amount

    def deposit(self,deposit:int):
        if deposit <= 0:
            raise ValueError("value invalid, just number positive")
        self.amount += deposit
        return f"deposit with sucess!"

    def withdraw(self,withdraw:int):
        if withdraw <= 0:
            return f"withdraw invalid,just withdraw numbers positive."
        elif withdraw > self.amount:
            return f"withdrawal denied,try again."
        self.amount -= withdraw
        return f"withdrawal with sucess. {self.amount}"

    def update_new_name(self,new_name:str):
        self.name = new_name.title()
        return f"new name this account is: {self.name}"

person1 = BankAccount("Natan",100)
person1.deposit(100)
person1.withdraw(50)
person1.update_new_name("dev natan")
print(person1.deposit(100))
print(person1.withdraw(400))
print(person1.update_new_name("dev natan"))