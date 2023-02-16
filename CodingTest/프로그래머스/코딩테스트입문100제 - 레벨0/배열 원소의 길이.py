def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

solution(["We", "are", "the", "world!"])

"""
다른사람코드
    def solution(strlist):
        answer = list(map(len, strlist))
        return answer
    -> map 사용!!
"""