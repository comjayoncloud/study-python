n = int(input())
a = list(map(int,input().split()))
a.sort()
count = 0
result = 0
#5번 진행
for i in range(0,n):
    count +=a[i]
    result += count

print(result)