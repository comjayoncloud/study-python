def solution(n, lost, reserve):
    answer = n
    a = len(lost)-len(reserve)
    # 잃어버린수와 가져온수가 똑같을경우
    if len(lost)==len(reserve):
        return n
    # 잃어버린 경우의 수가 더 많은경우
    elif a > 0 :
        return n
    elif a < 0 :
        return n-a
    return answer


solution(5,[2,4],[1,3,5])

"""
전체학생수 n
도난 당한 학생들 배열 lost
여벌의 체육복 가져온 학생들 reverse
"""