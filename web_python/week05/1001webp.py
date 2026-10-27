"bool공부"
bool()      #False
bool(0)     #False
bool([])    #False
bool(" ")   #True
bool([0])   #True

print(False/True)
print(False or True)
print((1,2,3) and "")
print([] or 0)

print(True)
bool(1)

"if문 공부"
grade,cheated=None,True
score=int(input("성적을 입력하세요:"))
if score >= 90:
    if not cheated:
        grade='A'
    else:
        grade='F'
else:
    grade="B"
print(f"당신의 성적은 {grade}입니다")

score=65

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
    
"Loop 공부" #Loop는 iterable이 중요함

students_no={"hanblanccoa":9,"dlgksruf":10,"sktlgus":0}
for numbers,babo in students_no.items():
    print(babo,numbers)
    
for a,b,c in [(1," ",3),(1,3,5),(3,4,5)]:
    print(a,b,c)
    
a,b,c=("하이","hi",["hanblanccoaT","goal"])
print(a,b,c)

a=(1)   #얘도 int임
print(type(a))
 
#range는 새로운 타입임
a=["p",'l','a','n','A']
for i in range(1,5): 
    print(a[i])
    
a={"Park":1,"Kim":2,"Lee":3}
for name,num in a.items():  #이렇게 하면 튜플로 나오지 않음
    print(name,num)
    
scores={"Kim":80,"Lee":90,"Park":100}
for name,score in scores.items():
    print(f"{name}:{score}")

    
for a,b,c in [(1,2,3),(4,5,6),(7,8,9)]:
    print(a,b,c)
    
    
a,b,c=[(1,2,3),4,"a"]
print(a,b,c)

i=[1,2,3,4]
print(i+10)

" "*(N-i-1)+"*"*(i+1)