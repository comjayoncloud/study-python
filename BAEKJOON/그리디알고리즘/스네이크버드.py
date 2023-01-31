n,l = map(int,input().split())
h = list(map(int,input().split()))

h.sort(reverse=False)
for i in range(n):
    if(l >=h[i]):   
        l +=1
    else:
        continue
print(l)