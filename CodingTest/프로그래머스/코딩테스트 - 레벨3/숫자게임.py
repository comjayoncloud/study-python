def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    for a in A:
        if a >= B[0]:
            continue
        else:
            answer += 1
            del B[0]
    return answer

solution([5,1,3,7],[2,2,6,8])


"""

걸린시간 : 15분

초기 생각한 해결방안 :
    승리 기준점은 B팀. 
    같으면 카운트 0 
    B가 더크면 카운트+1
    B 팀원들이 얻을 수 있는 최대 승점을 return 하도록 solution 함수를 완성해주세요.
    비교하기 쉽게sorted 활용

틀린점 및 해결방안 :
    없음

다른사람코드 및 리뷰 :
    
"""