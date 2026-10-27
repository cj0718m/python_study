def function7(s:str):
    has_digit=False
    has_lower=False
    has_upper=False
    
    for i in s:
        if i.isdigit():
            has_digit=True
        elif i.islower():
            has_lower=True
        elif i.isupper():
            has_upper=True
    return has_digit and has_lower and has_upper

print(function7('1234'))