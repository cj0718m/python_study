"문제 7"
class Person:
    def __init__(self,name,age=0):
        self.name=name
        self.age=age
    def get_name_upper():   #self인자가 들어갈 자리를 안만들어주어서 오류가 남
        return self.name.upper()

p=Person("Park",20)

print(p.get_name_upper()[-1])

"문제 8"
class Circle:
    def __init__(self,length):
        self.r=length
    def add(a,b):       #__add__라고 써야함
        return a.r+b.r

c1=Circle(10)
c2=Circle(5)
print(c1+c2)