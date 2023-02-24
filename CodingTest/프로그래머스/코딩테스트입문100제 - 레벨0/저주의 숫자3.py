def solution(n):
    answer = 0
    return answer

solution(15)


def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]
        
print(convert_notation(233, 3))