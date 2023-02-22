def solution(n):
    answer = []
    for i in range(1,n+1):
        if n%i==1:
            answer.append(i)
    
    return min(answer)

solution(10)
solution(12)

"""
다른사람코드
    def solution(n):
        return [x for x in range(1,n+1) if n%x==1][0]

분석 
    for문에서 바로 .. 코드가 간단해보인다

"""