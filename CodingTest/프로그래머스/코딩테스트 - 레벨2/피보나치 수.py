def solution(n):
    answer = []
    for i in range(n+1):
        if i == 0 or i==1:
            answer.append(i)
        else:
            f = answer[i-1]+answer[i-2]
            answer.append(f%1234567)
    return answer[-1]    



solution(3)


"""

걸린시간 : 10분

생각한 해결방안 :
    A.
    피보나치 0 1 1 2 3 5 ... 
    F0 = 0 
    F1 = 1
    F N = F N-1 + N-2
    1. 기준이 되어야하는 2개가 필요함 (0,1)
    2. 0,1을 넣고 그다음부턴 i-1 + i-2가 되므로 그 수를 배열에추가
    3. 마지막 원소

틀린점 :
    없음

다른사람코드 및 리뷰 :
    def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, (a+b)%1234567
    return a

    => 간단하게 코드를 짯다.
    해설)a,b=b,a+b 는 (a, b) = (b, a+b) 와 같습니다. 
    같은 위치에 있는 왼쪽 a에는 오른쪽 b값을, 왼쪽 b에는 오른쪽 a+b 값을 동시에 할당하라는 뜻입니다. 
    파이썬에서는 2개 이상의 복수의 변수를 동시에 상호 할당할 수 있습니다.
    
"""