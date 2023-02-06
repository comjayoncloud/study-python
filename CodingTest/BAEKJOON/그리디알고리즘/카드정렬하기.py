import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
card = []
for _ in range(n):
    heappush(card, int(sys.stdin.readline()))

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
파이썬에서 input은 메모리를 많이 잡아먹어서 시간초과가 뜬다. 고로 input대신
sys를 쓰자.

"""