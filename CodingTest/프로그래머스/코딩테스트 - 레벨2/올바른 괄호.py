def solution(s):
    temp = []
    for i in s:
        if i == '(':
            temp.append(i)
        else:
            if len(temp)>=1 and temp[-1]== '(':
                temp.pop()
            else:
                return False
    if len(temp)==0:
        return True

    return False

solution("(()(")
# solution("()()")
"""

걸린시간 : 23분

생각한 해결방안 :
    #A
    (,) 으로만 결과는 true or false
    ()만나면 사라짐 다사라졌을때 true ,아니면 false
    1. s에서 ()를 replace ''으로 바꿔주는게 좋을듯.반복문은 len(s)만큼
    2. len(s)의 길이가 0 이면 다 사라진거기 때문에 true , 아닐떈 false 리턴
    => 시간초과. 효율성 문제..for 문에서 s가 ''이 되었을때 break 걸어도 효율성 문제발생. 문제는 replace

    #B 
    (,)로만 되어 있기에. 카운트로 가볍게 하면될듯하다. )()( 경우 카운트는 같지만 오류가 생김.
    1. 비교할 임시 배열 temp [] 생성
    2. 기준을 '(' 로 잡았고 , ( 일때 temp에 원소 추가 , 그후 )가 들어올때 , temp 길이가 1 이상이며 마지막원소가 (와 같다면
       ')' 를 의미하기에 temp에서 pop해줌.
    3. 이후 len을 통해 비어 있으면 모두 없어진거기 때문에 True, 아닐시에 False  

틀린점 :
    def solution(s):
        for i in range(len(s)):    
            if '()' in s :
                s = s.replace('()','')
            elif s=='':
                break
        
        if len(s)==0:
            return True
        return False

    solution("()()")
    => replace 

다른사람코드 및 리뷰 :
    문제 제한사항에 s의 길이는 100,000 이하 였다. replace는 시간 초과가 잘일어나는 효율적이지 않은 코드인듯하다.

"""