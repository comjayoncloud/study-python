def solution(s):
    answer = []
    print(not(answer))
    for i in range(len(s)):
        print(s[i])
        if len(answer)==0:
            answer.append(s[i])
        elif s[i]==answer[-1]:
            answer.pop()
        elif s[i]!=answer[-1]:
            answer.append(s[i])
    
    if len(answer)==0:
        return 1

    return 0

solution("baabaa")
# => 효율성 테스트 통과 ,테스트케이스 13 실패
# => 9,10 라인 추가후 성공. 
"""

걸린시간 : 13분

생각한 해결방안 :
    모두 소문자, 모두제거가능하면 1(True) 아니면 0(False)
    2개붙어있는짝 찾음. 찾으면 지우고 앞뒤로 이어붙임
    baabaa -> b aa baa -> bb aa -> aa -> 없
    1. 첫숫자는 그대로넣음
    2. 다음 숫자가 그전에 마지막과 같으면 전꺼를 pop하고 배열에 넣지않음
    3. s의 len이 0 이되면 1 반환, 아니면 0반환

틀린점 :
    테스트케이스 13에 실패하였다. 문제 해결은 9,10라인을 추가함으로써 통과    
    s배열의 i번째 원소와 s배열의 마지막 원소가 같지 않을 경우를 생각하지 못했었음.

다른사람코드 및 리뷰 :
    def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)    
    return not(answer)

    => not(answer)은 True였다. 빈배열 체크하는경우다. 처음안 사실! 나의경우 len으로 빈배열인지 아닌지 확인했었음
       좀더 깔끔하다. 다른사람의 코드의 경우 43 , 46 .. else , else 로 append(i) 1번만 썻고
       나의 경우 elif elif 로 같은 코드를 2번 사용했기에 효율적이지않다고 느꼇다.
"""