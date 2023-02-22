def solution(a, b):
    answer = []
    for i,j in zip(a,b):
        answer.append(i*j)
    return sum(answer)

solution([1,2,3,4],[-3,-1,0,2])

"""
다른사람코드
    def solution(a, b):

        return sum([x*y for x, y in zip(a,b)])
"""