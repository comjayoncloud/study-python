def solution(n):
    answer = []
    for i in range(1,n+1):
        if i%2!=0:
            answer.append(i)
    return answer

solution(10)

"""
다른사람코드
    def solution(n):
        return [i for i in range(1, n+1, 2)]
"""