def solution(sides):
    answer = 0
    a = sides.pop(sides.index(max(sides)))
    for i in sides:
        if sum(sides) > a:
            answer = 1
        else:
            answer = 2
    return answer

solution([1, 2, 3])
solution([3, 6, 2])
solution([199, 72, 222])

#가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
# max(sides) < 나머지 1+1
# 변수는 무조건 3


"""
다른사람코드1
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2

다른사람코드2
def solution(sides):
    sides.sort()
    return 1 if sides[0]+sides[1]>sides[2] else 2
"""