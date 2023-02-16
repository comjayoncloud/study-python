def solution(n):
    answer = []
    for i in range(1,n+1):
        if i%2==0:
            answer.append(i)
    return sum(answer)

solution(10)


"""
다른사람코드

    def solution(n):
        return sum([i for i in range(2, n + 1, 2)])
"""