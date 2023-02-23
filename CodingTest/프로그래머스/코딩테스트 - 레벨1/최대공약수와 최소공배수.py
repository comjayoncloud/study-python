def solution(n, m):
    answer = []

    #최대 공약수
    for i in range(min(n,m),0,-1):
        if n%i==0 and m%i==0:
            answer.append(i)
            break
    #최소 공배수
    for i in range(max(n,m),(n*m)+1):
        if i%n==0 and i%m==0:
            answer.append(i)
            break
            
    return answer

solution(3,12)

"""
다른사람코드
    def gcdlcm(a, b):
        c,d = max(a, b), min(a, b)
        t = 1
        while t>0:
            t = c%d
            c, d = d, t
        answer = [ c, int (a*b/c)]
        return answer


분석 및 느낀점
    유클리드 호제법 또는 유클리드 알고리즘은 2개의 자연수 또는 정식의 최대 공약수를 구하는 알고리즘의 하나
"""