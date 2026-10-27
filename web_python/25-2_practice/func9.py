def function9(*args):
    result=0
    n=len(args)
    if n%2==0:
        for i in args:
            if i%2==0:
                result+=i
    else:
        for i in args:
            if i%2!=0:
                result+=i
    return result

print(function9(1,-1,-2,2))