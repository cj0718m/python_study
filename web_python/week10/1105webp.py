class Person:
    "This is Person Class"
    year=1
    def __init__(self,name):
        self.name=name
        
class Student(Person):

    def __init__(self,name,major):
        super().__init__(name)
        self.major=major

print(Person.__doc__)