from sympy.ntheory import factorint

def solution(n):
    print(list(factorint(n)))
    return list(factorint(n))

solution(12)


def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            answer.append(d)
            n = n // d
        else:
            d += 1
    return list(dict.fromkeys(answer))