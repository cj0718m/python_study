def func(n):
    L=[]
    while n<3:
        n+=1
    return L

print(func(1))

def divide(a,b=10):
    c=a/b
    return c

result=divide(a=1,2)    #포지셔널 방식으로 쓸거면 둘다 해야함,Syntax error
print(result)
