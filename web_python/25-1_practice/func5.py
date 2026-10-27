def function5(L1:list,L2:list):
    result=[]
    if len(L1)>len(L2):
        n=len(L2)
    else:
        n=len(L1)
    for i in range(n):
        result.append(L1[i]+L2[i])
    return result
    
print(function5([1,2,3],[-99,4]))
        