def solution(s):
    a = []
    for i in s:
        
        if a[-1:] == [i]: continue
        a.append(i)
    return a

solution([1,2,3,4,5,6,7])

"""
해결방안
    1. 빈배열 생성
    2. 빈배열과 s를 비교해서 같으면 넘어가고 없으면 빈배열에 추가

분석 및 느낀점
    list[-1:] 은 뒤부터 하나씩, 빈 배열에 써도 괜찮음.
"""