def function5(s1:set,s2:set,s3:set):
    result=0
    result=sum(s1&s2&s3)
    return result

print(function5({1,2,3},{2,4},{3,4}))



