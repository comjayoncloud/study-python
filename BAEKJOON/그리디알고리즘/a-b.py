A,B = map(int,input().split())

count = 0
while True:
    if(A==B):
        count +=1
        print(count)
        break
    else :
        if(A>B):
            print("-1")
            break
        elif(B%2==0):
            B = B//2
            count+=1
        elif(B%2!=0):
            B = int(str(B)[0:-1])
            count+=1


        


"""
# 162 -> 2로 바꿔보기 while문 사용
1. A==B 일경우 
2. A==B 가 아닐 경우
    2-1 : -1 이 나올 경우
    2-2 : B가 2의 배수일 경우
    2-3 : B가 2의 배수가 아닐경우 


"""


"""
남의 코드 : 
    삼항연산자를 이용해서 코드가 정말 간소화 되어있다. 
from sys import stdin

A, B = map(int, stdin.readline().split())
cnt = 1

while B > A:
    B = (B - 1) // 10 if B % 10 == 1 else B / 2
    cnt += 1

print(cnt) if B == A else print(-1)
"""