n=int(input()) #도시의 개수
km=list(map(int,input().split()))#도로의 길이
price=list(map(int,input().split()))#가격

minPrice=price[0]
total=0

for i in range(n-1):
    if minPrice>price[i]:
        minPrice=price[i]

    total+=(minPrice*km[i])
print(total)

"""
1. n,a,b 선언
2. 첫번째 원소들은 무조건 실행
3. 다음 원소부턴 b배열(가격)을 다음 것과 비교해서 곱해서 더하면됌  
"""

