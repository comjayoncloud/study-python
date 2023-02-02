n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)
cost = 0
for i in range(n):
    if(i%3!=2):
        cost += a[i]
print(cost)