a,b = map(int,input().split())
r = bool((not a and not b) or (a and b))
print(r)