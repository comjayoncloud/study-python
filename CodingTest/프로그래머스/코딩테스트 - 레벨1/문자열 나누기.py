def solution(s):
    answer = 0
    count=''
    count1=0
    count2=0

    for i in s:
        if count=='':
            count=i
            count1+=1
        else:
            if count==i:
                count1+=1
                
            else:
                count2+=1
                
            if count1==count2:
                answer +=1
                count =''
                count1=0
                count2=0
                
    if (count1 or count2) !=0:
        answer+=1

    return answer

# solution("banana")
# ba , na, na 
solution("abracadabra"	)
# ab ra ca da br a
# solution("aaabbacc ccabba"	)

# aaabbacc
# ccab 
# ba
"""

걸린시간 : 22분

초기 생각한 해결방안 :
    첫글자 읽고 그걸 x라 함.
    진행방향 -> x와 x가 아닌 다른글자들이 나온 횟수를 각각 셈. 처음으로 두 회수가 같아지는 순간 멈춤.지금까지 읽은 문자열을 분리.
    종료조건 1. s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복 남은 부분이 없으면 종료
    종료조건 2. 두 횟수가 다른 상태에서 더이상 읽을 글자가 없으면 분리하고 종료.
    
    x가 계속바뀜..

틀린점 및 해결방안 :
    없음
    
다른사람코드 및 리뷰 :
    def solution(s):
        answer = 0
        sav1=0
        sav2=0
        for i in s:
            if sav1==sav2:
                answer+=1
                a=i
            if i==a:
                sav1+=1
            else:
                sav2+=1
        return answer

"""