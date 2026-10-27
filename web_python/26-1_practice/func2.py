def function2(f:str):
    f=float(f)
    f=int(f)
    f=str(f)
    f=f[-1]
    return f

print(function2('789.123'))