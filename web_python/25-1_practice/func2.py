def function2(s:str):
    result=""
    for i in s:
        if i.isalpha():
            result+=i
    result=result.lower()
    return result

print(function2("A123b45c"))
            
    