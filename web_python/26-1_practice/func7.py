def function7(s:str):
    result={}
    for i in s:
        if i in result:
            result[i]+=1
        else:
            result[i]=1
    return result
print(function7("aaafvads"))