def function6(L:list):
    L.sort()
    if len(L)<2:
        return
    return L[len(L)-2]  #L[-2]

print(function6([-2,-9,3]))