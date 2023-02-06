def solution(before, after):
    if (sorted(before)==sorted(after)):
        result = 1
    else :
        result = 0
    return result


"""
다른사람 코드

def solution(before, after):
    return 1 if sorted(before)==sorted(after) else 0
"""

"""
느낀점 :
    삼항 연산자 사용 해보자
"""