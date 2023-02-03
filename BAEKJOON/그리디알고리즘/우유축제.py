# n = int(input())
# a = list(map(int,input().split()))
# count = 0
# for i in range(n):
#     if(a[i] ==  count%3):
#         count+=1
#     else:
#         continue
# print(count)

"""
딸기,초코,바나나를 a,b,c로 치환
규칙 : 
    처음으로 a
    a다음 b
    b 다음 c
    c 다음 a
    a -> b -> c -> a -> b -> c -> a ....
a 배열 안을 비교해서 , a->b->c->a ... 안맞으면 count 증가하지않음.
0->1->2->0->1->2

1 1 
"""
print (0%3)
print( 1%3)
print (2%3)
print(3%3)
