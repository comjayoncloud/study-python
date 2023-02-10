def solution(angle):
    answer = 0
    if 0<angle<90:
        answer = 1
    elif angle==90:
        answer =2
    elif 90<angle<180:
        answer =3
    else:
        answer =4
    return answer


"""
다른사람 코드1

def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer

다른사람 코드2

def solution(angle):
    if angle<=90:
        return 1 if angle<90 else 2
    else:
        return 3 if angle<180 else 4
"""