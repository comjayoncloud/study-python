def solution(emergency):
    answer = []
    a = sorted(emergency,reverse=True)
    for i in emergency:
        answer.append(a.index(i)+1)


    return answer

solution([3, 76, 24]) 
#         [76, 24, 3] => a배열
#         [1   2  3] => 결과표


"""
다른사람코드1:
    def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]

다른사람코드2:
    def solution(emergency):
        e = sorted(emergency,reverse=True)
        return [e.index(i)+1 for i in emergency]
"""

"""
느낀점 :
    index함수에대해 알게됨. 아직까지 한줄에 코드짜는것에 익숙치가 않다... 

"""