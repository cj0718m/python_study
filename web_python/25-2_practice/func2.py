def function2(s:str):
    result=""
    result=result.lower()
    for i in s:
        if i.isalpha():
            result+=i
    if result==result[::-1]:
        return True
    else:
        return False
    