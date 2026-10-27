def function9(x:int,y:int):
    x=str(x)
    y=str(y)
    if x[:4]==y or x[-4:]==y:   #슬라이싱
        return True
    else:
        return False
    
print(function9(111211,1111))