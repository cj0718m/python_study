class Cat:
    def __init__(self,name,height):
        self.name=name
        self.height=height
    
    def __add__(self,other):
        new_cat_name=other.name[:2]+self.name[:2]
        if self.height>other.height:
            new_cat_height=other.height/2
        else:
            new_cat_height=self.height/2
            
        new_cat=Cat(new_cat_name,new_cat_height)
        return new_cat
        
        
    
        
cat1 = Cat("Lucy", 30)
cat2 = Cat("Maggie", 20)
kitten = cat1 + cat2
print(isinstance(kitten, Cat))
#True
print(kitten.name)

print(kitten.height)