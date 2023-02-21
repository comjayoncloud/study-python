from collections import Counter

def solution(array, n):
    a = dict(Counter(array))
    for key,value in a.items():
        if key == n :
            return value
        
    return 0

solution([1, 1, 2, 3, 4, 5]	,1)


"""
다른사람코드
    def solution(array, n):
        return array.count(n)
"""