with open("account.txt",'w') as f:
    f.write(input("이름을 입력하세요:")+'\n')
    f.write(input("비밀번호를 입력하세요:"))
    
with open('account.txt','r') as f:
    name=f.readline().strip()
    password=f.readline().strip()
    while True:
        name1=input('(로그인확인용)이름을 입력하세요:')
        password1=input('(로그인확인용)비밀번호를 입력하세요:')
        if name==name1 and password==password1:
            print('Correct!')
            break
        else:
            print('Wrong')
    
        
        
         