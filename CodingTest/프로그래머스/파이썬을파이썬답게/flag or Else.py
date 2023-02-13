import copy
answer=''
A = [int(input()) for _ in range(5)]
B = copy.deepcopy(A)
for i in range(len(A)):
    if i ==0 :
        B[i] = A[i]
    else :
        B[i] = B[i]*B[i-1]
for i in A:
    for j in B:      
        if i*2%j ==0:
            answer='found'
            break
        else:
            answer='not found'
print(answer)

"""
문제 해결 과정
    1. 5개 받음 ( 2 4 2 5 1 ) A 배열
    2. 5개 받은것을 곱하기 ( 2 8 16 80 80 ) B배열
    3. A배열의 제곱근기준으로 B를 순차적으로 확인

느낀점 
    for문을 쓰지않으려고 여러가지 방법을 찾아보았는데 실패.. 
    reduce를 사용해보았지만 실패 . 나중에 파이썬이 더 익숙해지면 다시풀어봐야겠다.
    코드를 좀 더 간결하고 짧게 짜고 싶다. 
"""




