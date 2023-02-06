n = int(input())
a = list(map(int,input().split()))
d = []

# 빈배열 d에 24개 원소 0으로 초기화
for i in range (23):
    d.append(0)
# 10번 반복. j는 0부터 시작.
for j in range(n):
    d[a[j]-1]+=1
print(*d)




