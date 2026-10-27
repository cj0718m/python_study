def function9(*args:int):
    result=0
    if args:
        result=max(args)
        return result
    return result
    
print(function9(-1,-2,-3))