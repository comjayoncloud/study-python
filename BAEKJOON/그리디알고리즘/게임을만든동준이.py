n = int(input()) 
a = []
for i in range(n):
    a.append(int(input()))

count = 0

for i in range(n-1,0,-1):
    # print(i) 3 ,2 ,1
    if a[i] <= a[i-1]:
        count += a[i-1]-a[i]+1
        a[i-1] = a[i]-1

print(count)
# n 개의 레벨
# 클리어 할때마다 점수
# 플레이어 점수 = 클리어 하면서 얻는 점수의 합
# 레벨을 난이도 순으로 배치했지만 실수로 쉬운게 어려운 레벨보다 많이 받는경우도 만듬

