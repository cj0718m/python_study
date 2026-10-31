class Student:
    def __init__(self,name,score=0):
        self.name=name
        self.score=score
        if self.score<0:
            self.score=0
        
    def add_score(self,n):
        self.score+=n
        
    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=80:
            return "B"
        else:
            return "C"
        
    def __eq__(self, other):
        return self.score==other.score
    
    def __len__(self):
        return self.score
    
s1=Student('Kim',85)
s2=Student('Lee',85)
s3=Student('Park',-10)

s1.add_score(10)

print(s1.score)
print(s1.get_grade())
print(s1==s2)
print(len(s3))
        