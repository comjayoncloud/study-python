def solution(s1, s2):
    result = 0
    for i in s1:
        for j in s2:
            if i == j :
                result +=1
    return result

solution(["a", "b", "c"],["com", "b", "d", "p", "c"])

"""
다른사람코드
    def solution(s1, s2):
        return len(set(s1)&set(s2));
"""