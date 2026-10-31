class Account:
    def __init__(self,balance):
        self.balance=balance
    
    def deposit(self,money):
        self.balance+=money
    
    def withdraw(self,money):
        self.balance-=money
    
    def __eq__(self, other):
        return self.balance==other.balance
    
a1=Account(1000)
a2=Account(500)

a1.deposit(500)
a2.deposit(1000)

print(a1.balance)
print(a2.balance)
print(a1==a2)
        