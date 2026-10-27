def function10(*args, **kwargs):
    result=-1
    L=list(kwargs.values())
    L.sort()
    if len(L)>0:
        result=L[-1]
    return result

print(function10(1,2))
    