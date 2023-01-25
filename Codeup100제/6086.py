a = int(input())
sum = 0
count = 0
for i in range(a+1):
    sum +=i
    count +=1
    if sum >=a:
        break
print(sum)
