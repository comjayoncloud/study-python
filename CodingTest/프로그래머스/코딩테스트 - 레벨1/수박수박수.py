def solution(n):
    answer=[]
    a = "수"
    b = "박"
    for i in range(1,n+1):
        answer.append(i)
        
    for i in answer:
        if i%2==0:
            answer[answer.index(i)]=b
        else:
            answer[answer.index(i)]=a
    return ''.join(answer)


solution(3) #수박수
solution(4) #수박수박
# 홀수 수
# 짝수 박


"""
해결방안
    1. 1부터 입력 받은 숫자 만큼 새 배열에 int로 저장
    2. 홀수일때 "수", 짝수일때 "박" 이기에 int 배열을 순회하여 홀짝에 맞게끔 문자열 변환
    3. 문자열 변환 한 리스트를 join을 사용, str로 return

다른사람코드1
    def water_melon(n):
        str = "수박"*n
        return str[:n] 

다른사람코드2
    def water_melon(n):

        return "수박" * (n//2) + "수" * (n%2)

분석 및 느낀점
    슬라이싱 활용 및 다른 패턴도 있었다. 너무 1차원적으로 생각하지 않았나 생각한다.
"""