n = int(input())
i = list(map(int,input().split()))

i.sort()
result = 0
for j in range(len(i)-1):
    result += i[j]

print(result)