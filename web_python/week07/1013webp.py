def function4(a,*value):
    c=sum(value)
    return c

result=function4(1,2,3,4,5)
print(result)

def function5(a,*value,**info):
    k=(sum(value)+sum(info.values()))
    return k

result=function5(1,2,3,b=4,c=5)
print(result)

'팩토리얼 예제'
def factorial(n):
    if n==0:
        n=1
    for i in range(1,n):
        n*=i
    
    return n 
print(factorial(1))

def factorial1(n):
    result=1
    
    for i in range(1,n):
        result*=i
    return result

