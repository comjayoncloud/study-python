n = int(input())
a = [5,2]
count = 0
while True:
    if n%5 ==0:
        count += n//5
        break
    else :
        n-=2
        count +=1
    
    if n<0:
        break

if n<0:
    print(-1)
else:
    print(count)
"""
1. 거스름돈을 무조건 2와 5로 나누어서.
2. 5부터 나누기.

"""