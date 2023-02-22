def solution(n):
    n = list(map(int,list(str(n))))
    a = list(reversed(n))

    return a

solution(12345)


"""
다른사람코드
    def solution(n):
        return list(map(int, reversed(str(n))))

분석 및 느낀점
    한줄에 해볼려고했는데 파이썬은 map 타입도 있고 메서드도 각자 다 다르니.. 그 개념에 대해 좀 더 
    익숙해지고 기억해야 한다. 많은 문제를 풀다보면 자연스레 머리속에 들어올거같다
"""