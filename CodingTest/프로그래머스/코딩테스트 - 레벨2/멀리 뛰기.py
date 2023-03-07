

def solution(n):
    if n<2:
        return n
    answer = [0]*n
    answer[0]=1
    answer[1]=2
    for i in range(2,n):
        answer[i] = answer[i-1]+answer[i-2]
    return answer

# solution(4)
solution(3)


"""

걸린시간 : 3시 46분 ~ 3시 55분

초기 생각한 해결방안 :
    한번에 1칸 또는 2칸을 뛸수있다.
    모든 경우의수.
    answer[i] = answer[i-1]+answer[i-2]
    
틀린점 및 해결방안 :
    없음
    
다른사람코드 및 리뷰 :

"""