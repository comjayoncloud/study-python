n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
sum =0
j = 0
# 5번실행
for i in reversed(range(n)):
    sum += a[i]*b[j]
    j +=1
    
print(sum)

"""
1. 입력 받을 n 값과 배열 a,b 선언
2. a,b 배열 오름차순
3. 5번 실행 값
"""
############################################################
"""
구글링 중 괜찮다고 생각한 코드
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
S=0
for i in range(n):
    A_MAX = max(A)
    B_MIN = min(B)
    S += A_MAX * B_MIN
    A.pop(A.index(A_MAX))
    B.pop(B.index(B_MIN))
print(S)
"""
