def solution(s):
    s = list(s)
    a = len(s)//2
    #짝수일때
    if len(s)%2==0:
        return ''.join(s[a-1:a+1])
    #홀수일때
    else:
        return s.pop(a)
    return 0
solution("we")


"""
해결방안
    1. 입력값 문자열의 길이를 반으로 나눈다.
    2. 나눈 값이 짝,홀로 나뉨
    2-1 홀일떄 pop 으로 가져온다
    2-2 짝일때 ''.join(s[몫-1 : 몫+1])

다른사람코드
    def string_middle(str):
        return str[(len(str)-1)//2 : len(str)//2 + 1]


분석 및 느낀점
    변수를 쓰지도 않고.. 깔끔한거같다
"""

