def function4(s:str,n:int):
        result=0
        for i in s:
            if int(i) == n:
                result+=1
        return result
print(function4('12345',0))