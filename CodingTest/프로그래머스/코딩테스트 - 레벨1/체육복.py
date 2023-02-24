def solution(n, lost, reserve):
    
    a = len(lost)
    b = len(reserve)

    if a == b :
        return n
    elif a < b:
        return n
    elif a > b:
        print("1")


    return 0


solution(5,[2,4],[1,3,5])

"""
전체학생수 n
도난 당한 학생들 배열 lost
여벌의 체육복 가져온 학생들 reverse

1. 도난 당한수 == 더가져온수 그냥 n 리턴
2. 도난 당한수 < 더 가져온수 그냥 n 리턴

3. 도난 당한수가 더 많은경우
    3-1 
"""