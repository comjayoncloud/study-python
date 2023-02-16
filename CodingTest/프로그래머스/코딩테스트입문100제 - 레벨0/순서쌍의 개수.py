
#시간초과
# def solution(n):
#     count = 0 
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i*j ==n:
#                 count+=1
#     return count

# 성공
def solution(n):
    count =0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
        else:
            continue

    return count

solution(20)


"""
다른사람코드
    def solution(n):
        return len(list(filter(lambda v: n % (v+1) == 0, range(n))))
"""