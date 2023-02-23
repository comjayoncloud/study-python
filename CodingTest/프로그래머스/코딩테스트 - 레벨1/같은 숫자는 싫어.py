def solution(s):
    a = [1,2]
    print(a[-1:])
    for i in s:
        
        if a[-1:] == [i]: continue
        a.append(i)
    return a

solution([1,2,3,4,5,6,7])

"""
해결방안
    A. for 문돌려서 다음께 하나있으면 하나로 바꿈
"""