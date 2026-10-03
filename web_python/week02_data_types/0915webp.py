print(0.000001)
a="I love 'python'"
print(a)
b='I love "you"'    #따옴표 다른걸로 써야함
print(b)

a="Hello"
b="World"
print(a+b)
print(a+" "+b+"?")
print(a*0)  #글자를 없애기,또한 음수도 보이지 않음
print(a*-2)

a='Hello\nworld'  #이스케이프문자 출력하고싶은 문자 앞에다 붙이기
print(a)

"https:\\예제 출력하는법"
text=r"Https:\\바보.com"
print(text)

s1="Hello world!"
s2=s1[-1:-13:2] #빈 문자열 발생
print(s2)
print(s1[-13])
s1="Nmixx"
s2=s1.upper()
s3=s1.lower()   #대문자로 바꾸기,특수기호는 대소문자 안봄
print(s1,s2,s3)

s="Hello world"
s[len(s)-12]

s1="nmixx"
s2=s1.count("i")
print(s2)

s="aespa"
s=s.strip("aa")  #양쪽에서 지워주기
print(s)

s1="aespa 123"
s1=s1.isalnum() #isalnum은 문자+숫자"만"!! 공백은 false나옴
print(s1)

name="Babo"
ilove="Minju"
print(f"저는 {name}이고 저는 {ilove}를 좋아합니다.")

a='babo1@'
b="babo1@"
print(a==b,a is b)  #특수문자가 붙으면 주소가 달라질수있다는점 기억해두기