def fucn1(s:str):
    n=s.strip()
    result=""
    for i in n:
        if i.isalnum():
            result+=i
    result=result.upper()
    return result

print(fucn1('  a-123    '))