"1번 문제"
result=0
for n in [1,2,3]:
    result=n
    
print(result)   #3,반복문 마지막에 변수가 저장됨,시간이 없어서 못품

"2번 문제"
result=0
for n in (1):
    result=n
    n=2
    
print(result)

"3번 문제"
result=0
for a,b in (1,2):
    result=a+b
    
print(result)   #Error 발생,int는 unpack 불가하기 때문에 error발생

"4번 문제"
result=0
for con in [True,False]:
    if con:
        result+=100
        
print(result)   #첫번째 원소가 true라 밑에 if문이 작동하고 100을 더하고 두번째가 False라 if 실행x 되고 종료돼서 result가 100임.

"5번 문제"
result=0
for num in {1,2,3}:
    result+=num
    
print(result)   #순서는 모르나,각각 1,2,3이 더해져서 최종 result값은 6이 됨.

"6번 문제"
result=0
for num in {[1],{2},(3,)}:
    result+=num[-1]
    
print(result)   #set는 순서가 없기때문에 인덱싱을 지원하지 않기 때문에 오류발생함.

"8번 문제"
L=[(1,2),(3,4),(5,5)]
total=0

for a,b in L:
    if a==b:
        total=a+b
        
print(total)    #5==5이기 때문에 10이 되서 정답은 10,잘못선택함

"10번 문제"
L=[1,2,3]
count=0
for n in L:
    count+=1
    L.clear()
    
print(count)    #첫번째 반복 이후 []빈 리스트가 돼서 오류가 발생할줄 알았으나,빈 리스트면 0회 반복이기 때문에 카운트 1인상태로 종료함.

"13번 문제"
count=0
for i in range(3):
    for j in range(3):
        count +=1
        break
    
print(count)    #안쪽의 for 문이 break로 종료되어도 위의 for 문의 0,1,2까지 반복되는건 초기화되기 때문에 count에 3이 더해져서 3임.

"18번 문제"
count=0
for i in range(3):  #0,1,2까지 반복
    if i==1:
        continue
    else:
        for j in range(3):
            count+=1
        break
        
print(count)    #break가 j for문에 적용된다고 생각했었음,그러나 들여쓰기 수준이 다르기 때운에 i for문에 적용되어서 답은 3.