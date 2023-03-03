def solution(dartResult):
    answer=''
    answer2=[]
    
    sdt = {"S":1,"D":2,"T":3}
    for i in dartResult:
        if str.isdigit(i)==True:
            answer +=i
        elif i in sdt:
            answer2.append(int(answer)**sdt[i])
            answer=''
            print(answer2)
        elif i =="*":
            answer2[-2:]= [s*2 for s in answer2[-2:]]
        elif i =="#":
            answer2[-1] = -answer2[-1]
    return sum(answer2)

solution("1S2D*3T")


"""

걸린시간 : 50분

초기 생각한 해결방안 :
    1제곱 S
    2제곱 D
    3제곱 T
    * = *2
    # 해당점수 마이너스
    *# 가능
    S,D,T 하나씩
    *,# 는 점수마다 둘중 하나만 존재할수 있음
    
    
    1. 계산할 문자열과 그 결과를 담을 배열선언
    2. S,D,T는 쉽게 dictonary로 만듬
    3. 계산
    3-1 숫자면 문자열에 넣음
    3-2 sdt면 제곱근만큼 곱해서 배열에 넣고 문자열은 초기화
    3-3 #와 * 조건 넣음
    3-4 배열원소들을 다 더함
 

틀린점 및 해결방안 :
    없음

다른사람코드 및 리뷰 :
    import re

    def solution(dartResult):
        bonus = {'S' : 1, 'D' : 2, 'T' : 3}
        option = {'' : 1, '*' : 2, '#' : -1}
        p = re.compile('(\d+)([SDT])([*#]?)')
        dart = p.findall(dartResult)
        for i in range(len(dart)):
            if dart[i][2] == '*' and i > 0:
                dart[i-1] *= 2
            dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

        answer = sum(dart)
        return answer

    => 정규 표현식을 사용했다..정규 표현식 사용 방법이 아직 너무 어려워보임 ;
"""