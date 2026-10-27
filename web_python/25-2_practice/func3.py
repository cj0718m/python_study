def function3(x:int,y:int):
    count=0
    n=y
    while n < x:
        n+=y
        count+=1
        
    return count

print(function3(99,25))