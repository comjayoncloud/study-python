from math import factorial

def solution(n):
    answer = 0
    while True:
        answer += 1
        b = factorial(answer)
        if b == n:
            print(answer)
            break
        if b > n:
            answer -=1
            break
    return answer


solution(3628800)
solution(7)

"""
다른사람코드
    from math import factorial

    def solution(n):
        k = 10
        while n < factorial(k):
            k -= 1
        return k
"""