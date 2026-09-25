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


