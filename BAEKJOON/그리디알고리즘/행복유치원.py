# n 은 명수 , k는 그룹 개수
n,k = map(int,input().split())

# 키를 받을 배열
a = list(map(int,input().split()))
costs = []
for i in range(n-1):
    costs.append(a[i+1]-a[i])
costs.sort()

cost = 0
for i in range(n-k):
    cost += costs[i]
print(cost)

# 최소비용? sort해서 가장작은값 다음 - 가장 작은값 = 최소

