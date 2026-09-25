"% string 연습"
name=str(input("이름을 입력하세요:"))
age=int(input("나이를 입력하세요:"))
s="My name is %s and I am %d"%(name,age)
print(s)    #%s는 str,%d는 int,%f는 float

"str.format()연습"
n,a="Babo",20
s1="My name is {} and I am {}".format(n,a)
print(s1)

"f-string연습"
k,j="Babo",20
s="My name is {k} and I am {j}"
print(s)

"Id 연습"
a="Hello"
b=a
c="Hello"
print(id(a),id(b),id(c))

a=999
b-999
print(id(a),id(b))

a,b=999,999
print(id(a),id(b))

"==,is 연습"
a=10
b=10.0
print(a==b) #True,크기는 같음
print(a is b)

"List 연습"
var1=["a","b",1234]     #int,float은 따로 출력 불가
print(var1)

var2=["Babo","World",1234]
print(var2[0][3])

num=[1,2,3,4]
num[-1]=["khu"]
num[-2]="khu"   #둘의 차이 제대로 알기
num[1:-1]=["babo","bup"]    #범위를 지정하고 하는것과 그냥 지정하는것은 다름
print(num)


students=["aa","bb","cc","dd"]
students[1:-1]=["babo","ddonggae","Liv"]
students[1:-1]=[1234]   #int는 교체 불가
print(students)
#str

a=[1,2,3,4]
b=a.copy()  #카피는 똑같이 생긴것을 새로 하나 만드는것 생긴것은 똑같지만 주소가 다름
print(a is b,a==b)

a=[1,2,3,4,5]
a[1:-1]="리센느"
print(a)

students=["a","b","c","d"]
students[1:3]=["e","f","g"] #구간 지정해서 넣어줄때에는 list 아님
print(students,students[2])

students=["a","b","c","d"]
students[1]=["e","f","g"] #그냥 넣어줄때에는 list임
print(students,students[2])

students = ["AKMU", "DAY6", "IVE", "YOUNHA"]
students[1:-1]=["바보똥개","멍청이"]   #잘라서 넣는다
print(students)

students = ["AKMU", "DAY6", "IVE", "YOUNHA"]
students[1:-1]=[["바보똥개","멍청이"]]
print(students)

list=["nana","babo"]
list.append([100]) #append는 무조건 한개만
print(list)

a=[1,2,3,4,5]
x=a.pop(3)  #뺀 값을 x에 저장
print(a,x)  #list는 수정됨
