from collections import Counter

def solution(array):
    answer = []
    a= Counter(array)
    b = max(a.values())
    for (key, value) in a.items():
        if value == b :
            answer.append(key)
    if len(answer)>=2:
        return -1    
    return answer[0]

solution([1, 2, 3, 3, 3, 4])


"""
다른사람코드1
    def solution(array):
        while len(array) != 0:
            for i, a in enumerate(set(array)):
                array.remove(a)
            if i == 0: return a
        return -1
"""