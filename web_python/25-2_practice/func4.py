def function4(L1:list,L2:list):
    result=set(L1)&set(L2)
    return result

print(function4([1,1,2,2,3,3,3],[1,2,3,4]))