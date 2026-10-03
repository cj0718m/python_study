"1번째 문제"
result= True or False
print(result)   #True가 나와야하는데 True의 값이 1이니까 1을 출력해야하는줄 알고 1으로 선택함

"2번째 문제"
score=100
if score=100:   #이 부분에서 문제가 발생,==으로 해야하는데 =으로 해서 Error발생함,함정같은 문제!
    print('A+')
    
elif score>90:
    print("A0")
else:
    print("F")

"3번째 문제"    
L=[0]

if L:
    L.append(1)
if L:
    L.clear()
if L:
    L.append(3)
    
print(sum(L))   #if 세개니까 따로따로 분석 그래서 두번째 if 실행하고 빈 list가 되고 세번째 if는 실행되지 않음.