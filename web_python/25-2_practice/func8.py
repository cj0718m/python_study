def function8(s:str):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    L=list(d.values())
    L.sort()
    result=L[-1]
    return result

print(function8("[1,2,3,45,5]"))




       