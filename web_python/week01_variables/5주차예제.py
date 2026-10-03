d={"Park":10,'Pa':20,'rk':30}
print(d['Pa'+'rk']) #d['Park']랑 똑같음

a={'Park':100}
b={'Kim':100}
print(a+b)  #dictonary끼리는 합/차가 안됨

score={}
team1=['Park','Kim']
team2=['Lee','Hong']
score[team1]=100
score[team2]=100
print(score[team1]/score[team2])    #dictonary의 key는 무조건 immutable 해야함 int,str,tuple

score={}
team1=('Park')  #이건 튜플이 아님 str임 왜냐면 쉼표가 없으니까
team2=('Kim')
score[team1+team2]=100
print(score[team1,team2])   

score=["Park"]
print(score)
s=str(score[:]) #리스트 출력 기억 잘하기
print(s)

b=["park"]  #list
print(b,type(b))
b={"park"}  #set
print(b,type(b))
b="park"
print(b,type(b))
b=('park')  #str
print(b,type(b))
b=("park",) #tuple
print(b,type(b))

L1=[1,[2],(3,),{4}]
L2=L1.copy()
L1[1]=[2.0]
L1[3].add(5)
print(L1,L2)