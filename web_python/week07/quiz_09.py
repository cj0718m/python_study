"문제 1"
def union(a,b):
    c=a+b
    return c

result=union({1},{2})   #set끼리는 연산이 안됨 그러므로 출력은 error
print(result)

"문제 3"
def plus(a,b,c):
    n=a+b+c

result=plus([1,2,3])    #()안에 하나의 인자만 들어있으므로 나머지 b,c는 할당이 되지 않아서 오류발생
print(result)

"문제 4"
def func(t1,t2):
    return t1,t2

result=func((1,2,3),(4,5))  #t1,t2를 반환할때 튜플 형태로 반환함,그러므로 return값은 ((1,2,3),(4,5))라는 원소가 두개인 튜플
print(result[1:])           #마지막 출력값도 ((4,5),)인 이유는 (4,5)을 원소로 갖는 튜플이여야하므로 ((4,5),)임.

"문제 12"
def func(a,*b,c,**d):
    return c
    
result=func(1,2,3,b=5,c=6)
print(result)   #error가 난다 했는데 그냥 b와 *b는 다르기 때문에 헷갈려서 틀림.



