ㅁㅁㅁ@@@=20   #특수기호는 다 안되지만 언더바는 됨
print(ㅁㅁㅁ@@@)

import keyword  #변수이름이 안되는것들
print(keyword.kwlist)

if=100
print(if)   #안되는예시들

print = 100   #프린트는 예외지만,쓰지말길
print(print)

del print   #프린트에 있는값을 지워주는것

print("Aa")

IF=100  #대문자는 상관없음
print(IF)

a,b,c=1,2,3
print(a,b,c)

a,b=b,a
print(a,b,c)

a=3
a+=9999 #다양한 연산자 가능
print(a)

a=99
b=3
print(id(a))    #주소(id로 알아내기)
print(type(id(b)))

Fahrenheit=float(input("화씨온도를 입력하세요:"))
Celsius=((Fahrenheit-32)*(5/9))
print("섭씨온도로 계산한 결과는",Celsius,"입니다.")

a=3.0
b=3
c=a*b
c=int(c)    #반올림 안함,그냥 정수부분만 남겨두는것
print(c,type(c))

a=4
b=2
c=a/b
print(c,type(c))    #나눗셈은 무조건 실수형으로 나옴 나머지가 0이여도
#정수와 소수랑 계산하면 소수가 이김
#나머지 연산은 다름

s="1234.56"
print(s,type(s))
s=float(s)  #한번에 정수(int)로 바꿔주지 않음
print(s,type(s))
s=int(s)
print(s)    

a=0.1+0.2
b=0.3
print(a==b) #False나옴 이진수->무한소수->십진수 변환에 잘못됨(Rounding Error)
