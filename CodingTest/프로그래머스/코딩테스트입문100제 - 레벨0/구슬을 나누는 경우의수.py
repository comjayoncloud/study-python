from math import factorial

def solution(balls,share):
    n = factorial(balls)
    m = factorial(share)
    bottom = factorial(balls-share)*m
    return n/bottom


"""
다른사람코드1
    import math
    def solution(balls, share):
        return math.comb(balls, share)
    ->오.. math에 이런게 있었다니?

다른사람코드2
    def solution(balls, share):
        answer = factorial(balls) / (factorial(balls - share) * factorial(share))
        return answer

    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result = result * i
        return result

"""