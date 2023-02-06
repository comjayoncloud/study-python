def solution(my_string):
    answer = []

    a = list(my_string)
    for i in a:
        if i.isdigit()==True:
            answer.append(int(i))
    answer.sort()    
    return answer


"""
다른사람 코드:

def solution(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))
"""

"""
다른사람코드 2:
def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])
"""

"""
느낀점 :
    lambda 함수를 사용하는 버릇을 해보자. 
"""