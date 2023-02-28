def solution(n):
    # answer = 79
    answer = n+1
    
    while True:
        if answer.count('1') == bin(n).count('1'):
            return answer
        answer+=1

solution(78	)

"""

걸린시간 : 10분

생각한 해결방안 :
    1. 받은 n을 2진수로 변환
    2. 바뀐 2진수의 다음 큰수를 구함. 1의 개수는 같음
    2-1 받은 n 진수의 카운트 '1' 과 같은 수를 구해야함. 문제는 n보다 큰수를 구해야하기에 , n+1부터 시작
    2-2 while 문을 써서 answer 계속 증가. 증가하면서 '1'과 같은수를 찾으면 return
틀린점 :
    없음
다른사람코드 및 리뷰 :
    다른 코드 들을 보았는데 다 2진수라는 단어가 나오자 bin을 씀.

"""