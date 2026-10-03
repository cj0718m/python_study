students=["Park",'Kim','Lee']   #인덱싱,슬리이싱 가능한거만 가능
for i in :
    print(i)
    
word="Word"
for i in word.upper():
    print(i)
    
st={'Babo':100,'Kim':99,'minami':999}
for name,number in st.items():
    print(f"{name} have {number}")

d=['Mi','na','mi']
for i in range(1,10):
    print(d)

for i in range(0,3):
    print("i value is:",i)
    for j in range(3,6):
        print("i=",i,"j=",j,"i*j=",i*j)
        
    
for num in range(4):
    print(num)

    for num2 in range(10):
        if num2 > 5:
            break
    else:
        print("dasdsd")
        
for num in range(4):
    print(num)
    
L=[10,20,30]
for element in enumerate(L):
    print(element)
