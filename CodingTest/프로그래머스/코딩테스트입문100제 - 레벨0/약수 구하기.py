def solution(n):
    answer = []
    for i in range(1,n+1):
        for j in reversed(range(n+1)):
            if i*j ==n:
                answer.append(i)
    return answer

solution(24)


"""
다른사람코드1
    def solution(n):
        answer = [i for i in range(1,n+1) if n%i == 0]
        return answer

다른사람코드2
    def solution(n):
        return list(filter(lambda v: n % v == 0, [i for i in range(1, n//2+1)])) + [n]
"""