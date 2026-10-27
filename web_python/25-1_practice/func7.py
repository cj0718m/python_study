def function7(s:str):
    has_digit=False
    has_upper=False
    has_lower=False
    for i in s:
        if i.isdigit():
            has_digit=True
        elif i.isupper():
            has_upper=True
        elif i.islower():
            has_lower=True
    if has_digit and has_lower and has_upper:
        return True
    else:
        return False

print(function7('123abcC'))