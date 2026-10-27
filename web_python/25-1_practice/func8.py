def function8(L:list):
    result={}
    k=set(L)
    for i in k:
        result[i]=L.count(i)
        
    return max(result,key=result.get)


print(function8([0,1,0,10,10,1,3,11,0]))