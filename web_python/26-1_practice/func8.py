def function8(a:int,b:int,c:int):
    L=[a,b,c]
    L.sort()
    if L[2]**2==L[0]**2+L[1]**2:    #제곱은 ^가 아니라 **임
        return True
    else:
        return False
    
print(function8(1,2,3))