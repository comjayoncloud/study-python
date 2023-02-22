def solution(a, b):
    answer = 0
    arr = sorted([a,b],reverse=False)
    for i in range(arr[0],arr[1]+1):
        answer +=i
    return answer

solution(5,3)

"""
다른사람코드
    def adder(a, b):
        if a > b:
            a, b = b, a
        return sum(range(a, b + 1))

다른사람코드2
    def adder(a, b):
        return (abs(a-b)+1)*(a+b)//2

분석 및 느낀점
    다양한 방법이 있다 
"""