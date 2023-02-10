def solution(money):
    answer = []
    answer.append(money//5500)
    answer.append(money%5500)
    return answer

"""
다른사람 코드
def solution(money):
    answer = [money // 5500, money % 5500]
    return answer
"""

"""
다른사람 코드2
def solution(money):
    return divmod(money, 5500)
"""


"""
느낀점 :
    하나씩 append 하는것보다 한줄의 코드 혹은 divmod를 쓰자
    divmod는 몫 , 나머지값
    하지만 divmod가 항상좋은것은 아니다.
    작은 숫자를 다눌땐 a//b ,a%b 보다 느리고 가독성의 차이점도 있을수 있다.
    
"""