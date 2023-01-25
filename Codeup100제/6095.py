# 모범 답안
d=[]
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)
n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    d[x][y]=1

for i in range(1,20):
    for j in range(1,20):
        print(d[i][j],end=' ')
    print()

# 우리밋코드
n = int(input())
shape = [[0 for _ in range(19)]for _ in range(19)]
for _ in range(n):
    x,y = map(lambda num : int(num)-1,input().split())
    shape[x][y]=1

for s in shape :
    print(*s)