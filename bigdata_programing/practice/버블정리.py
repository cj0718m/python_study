numbers = [7,3,9,1,5]

k=len(numbers)
for i in range(len(numbers)):
    for j in range(k-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
    k-=1

print(numbers)