from heapq import heappush, heappop

n = int(input())
card = []
for _ in range(n):
    heappush(card, int(input()))

count = 0
for i in range(n-1):
    temp1 = heappop(card)
    temp2 = heappop(card)
    count += temp1+temp2
    heappush(card, temp1+temp2)

print(count)

"""
heapq 없이 해볼려햇는데 너무 복잡..
heapq : 2진트리. 작은수 (루트)
"""