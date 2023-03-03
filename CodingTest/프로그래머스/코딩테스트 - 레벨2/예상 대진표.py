def solution(n,a,b):
    answer = 0
    while a!=b:
        answer +=1
        a,b = (a+1)//2 , (b+1)//2
        # 1라운드 후 2, 4
        # 2라운드 후 1, 2
        # 3라운드 후 1, 1

    
    return answer

"""

걸린시간 : 5시 20분 ~ 

초기 생각한 해결방안 :
    n 명 참가 . a 참가자번호 . b 참가자 번호 
    a != b


틀린점 및 해결방안 :
    없음
    
다른사람코드 및 리뷰 :
    def solution(n,a,b):
        return ((a-1)^(b-1)).bit_length()
"""