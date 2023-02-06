# 내 답안
n = int(input())
a = list(map(int,input().split()))
a.reverse()
print(*a)


# 모범 답안
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

for i in range(n-1, -1, -1):
  print(a[i], end=' ')