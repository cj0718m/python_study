class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def get_area(self):
        return self.width*self.height
    def is_square(self):
        return self.height==self.width
    def __eq__(self, other):
        return self.get_area()==other.get_area()
    
r1 = Rectangle(3, 4)
r2 = Rectangle(2, 6)
r3 = Rectangle(5, 5)

print(r1.get_area())
print(r3.is_square())
print(r1 == r2)
        

