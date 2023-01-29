n = int(input())
compare =0
count = 0
for i in range(1,n+1): 
    if compare+i>n:
        break

    compare += i
    count +=1


print(count)

"""
남들이 짠 코드중 괜찮은것:
    while문 사용.
s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)
"""

"""
남들이 짠 코드 :
    for문 똑같이 사용 . 나와 다르게 더 커졌을때 -1을 넣어줌.
s = int(input())
N = 0
result = 0
for i in range(1,s+1):
    result += i
    N += 1
    if(result > s):
        N -= 1
        break;
print(N)
"""