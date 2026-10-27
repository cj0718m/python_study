def function10(*args:int, **kwargs:int):
    result=0
    for i in kwargs:
        if i[0]=="a":
            result+=kwargs[i]
    return result
            
print(function10(1,2,ace=10,b=7,a21=100))