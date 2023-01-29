n = int(input())

t = [300,60,10]
a = []

if n%10 !=0:
        print("-1")
else:
    for i in t:
        a.append(n//i)
        n = n%i
print(*a)