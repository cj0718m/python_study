class Person:
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def plus(self):
        return 1+1
    
p1=Person('Park')
print(p1.get_name())
print(p1.plus())