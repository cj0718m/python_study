class Person:
    def __init__(self,name,height=30):  #height=30으로 매개변수 기본값 설정
        self.name=name
        self.height=height
        if self.height<30:
            self.height=30
    def get_upper_name(self):
        return self.name.upper()
    def __eq__(self, other):
        return self.name==other.name
    def __len__(self):
        return self.height
    
p1=Person('kim',175)
p2=Person('kim',20)
p3=Person('lee')

print(p1.get_upper_name())
print(p1==p2)
print(len(p1))
print(len(p3))      

  