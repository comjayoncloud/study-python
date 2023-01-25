a,b,c,d = map(int,input().split())
result = round(a*b*c*d/8 /1024 /1024,1)

print(result,"MB")