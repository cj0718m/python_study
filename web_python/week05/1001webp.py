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
    
for i in range(5):
    print(i)
    if i==3:
        print("3찾았다")
        break
else:    
    print("3을 못찾았다")
    
for i in range(5):
    print(i)
    if i == 2:
        break
else:
    print("반복 끝!")