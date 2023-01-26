n = int(input())

count = 0
while (n>=0):
    if(n%5==0):
        count+=n//5
        print(count)
        break
    n -=3
    count += 1
else:
    print("-1")


#느낀점:
# if 로만 고집하려고 하니.. 모든 조건을 만족하는 코드를 짜기엔.. 너무복잡해지고
# 구현하기 어려웠다. if와 while문 같이 쓰는 방법은 정말 효율적이였다.