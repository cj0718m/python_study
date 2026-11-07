class Person:
    def __init__(self,name):
        self.name=name
        
    def introduce(self):
        return f"My name is {self.name}"
    
class Student(Person):
    def __init__(self,name,major):
        super().__init__(name)
        self.major=major
    def introduce(self):
        return super().introduce()+f", I major in {self.major}"
    
class KHUStudent(Student):
    year=1
    
    @classmethod
    def set_year(cls,year):
        cls.year=year

s = Student("Kim", "CS")
k = KHUStudent("Park", "BigData")

KHUStudent.set_year(2)

print(s.introduce())
print(k.introduce())
print(KHUStudent.year)