n = int(input())
d = []
for i in range(n):
    d.append(int(input()))     

d.sort(reverse=True)

for i in range(n):
    d[i] = d[i]*(i+1)

print(max(d))