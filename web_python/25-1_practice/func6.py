def function6(n1:int,n2:int):
    n1=str(n1)
    n2=str(n2)
    n=len(n2)
    if n1[:n]==n2 or n1[-1:-n]==n2:
        return True
    else:
        return False
    
print(function6(71234562,2345))