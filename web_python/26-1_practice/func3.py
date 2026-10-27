def function3(s:str):
    result=""
    for i in s:
        if s.isalpha():
            result+=i
    result=result.lower()
    if result==result[::-1]:
        return True
    else:
        return False
print(function3('a12a'))