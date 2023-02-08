def solution(order):
    answer = 0
    if '3' in str(order):
        answer += str(order).count('3')
    if '6' in str(order):
        answer += str(order).count('6')
    if '9' in str(order):
        answer += str(order).count('9')

    return answer


"""
다른사람코드

def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
"""