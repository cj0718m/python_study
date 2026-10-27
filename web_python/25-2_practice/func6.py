def function6(n:int):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

print(function6(5))