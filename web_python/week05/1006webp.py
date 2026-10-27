L=[1,2,3,4,5]

def function1(L):
    return sum(L[-1:])


#result=function1(L)    
#print(result)

def opreation(a,b):
    plus=a+b
    minus=a-b
    return plus,minus

result=opreation(1,2)   #tuple로 여러 값들을 반환함
print(result)
    