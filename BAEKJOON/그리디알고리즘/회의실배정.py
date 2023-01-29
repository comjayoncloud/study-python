# 몇번 실행할지와 시작,끝시간 받을 배열 
n = int(input())
d = []
for _ in range(n):
    s,e = map(int,input().split())
    d.append([s,e])

# 회의실 들어갈때 올라갈 카운트 변수와 
count =0
last = 0

# 1. 2. 번 오름차순 두번 실행
d = sorted(d,key=lambda a:a[0])
d = sorted(d,key=lambda a:a[1])

# 배열만큼 실행. i는 시작시간 j는 끝나는시간.
for i,j in d:
    if i >= last:
        count +=1
        last = j 
print(count) 

"""
1. 시작시간으로 오름차순
2. 다시 끝나는 시간으로 오름차순

"""

