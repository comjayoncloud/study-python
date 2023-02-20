def solution(n):
    n=str(n)
    result = 0
    for i in n:
        result +=int(i)

    return result


solution(1234)

"""
다른사람코드
    def solution(n):
        answer = sum(list(map(int,list(str(n)))))
        return answer
"""