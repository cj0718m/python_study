#list.append()
var1=[1,2,3]
var1.append([4])
print(var1)
var1.append(4)
print(var1)
#list.extend(List)
var1=[1,2,3]
var1.extend([1,2,3,4])    #.extend()의 괄호안에는 무조건 리스트,출력시 결과 리스트 x
print(var1)
#
var1,var2=[1,2],["둘","넷"]
var1.sort()
var2.sort()
print(var1,var2)
#메모리 연습
students=["a","b","c","c"]
students[0]="e"
students[1]="f"
students[3]=[1,2]
people=students.copy()
people[0]="A"
print(people[0],students[0])
people[3][0]+=5
print(people[3],students[3])    #copy가 제대로 안됨 리스트는 각자도생하지 않음
#tuple 연습
var1=(1,2,3)
print(var1)
var1[0]=3   #튜플은 못바꾸심

a=(4)
print(a,type(a))

a=(4,5)
print(a,type(a))

#Common Sequence Operations
L=[1,2,3]
result=1 in L
print(result)

L=["a","v","b"]
result=max(L)
print(result)

#set(집합)연습
T=(1,2)
var3={T,"tree"}
print(var3)
#set 할려면 set() 해주면됨 튜플->세트 가능

#dictionary
score={"kim":80}
score[("Park","Lee")]=100
score["Hong"]=40
print(score[("Park")])

student_no={}
student_no["Bobo"]=100
student_no["Hello"]=99
print(student_no)


#pacing,unpacking 연습
data="Python",2026,"KHU"
a,*b=data   #*뒤에붙은것부터 리스트로 쭉 가져오기
print(a,b)

data=("Python","C","Python","Java")
print(data.count("Python"))
print(data.index("Python"))     #Python이 두개있지만 처음위치만 반환함.

"set연습"
numbers={1,2,2,2,3,4,5,6}   #set는 중복허용 X
print(numbers)  #set는 index 불가(당연하긴함)
"set연산자 연습"
A={1,2,3}
B={3,4,5}
print(A & B)    #교집합,결과는 set로 나옴

A={1,2,3}
B={3,4,"바보"}
print(A|B)  #합집합

A={1,2,3}
B={3,4,"바보"}
print(A-B)  #차집합 

"Dictionary 연습"
student = {
    "name": "찬주",
    "age": 21,
    "major": "빅데이터응용학과"
}
student["age"]=100
print(student["age"])