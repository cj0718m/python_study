def function3(L:list):
    n=len(L)
    if n%2==0:
        result=L[-1]
        return result
    else:
        result=L[0]
        return result
    
print(function3([0,100]))