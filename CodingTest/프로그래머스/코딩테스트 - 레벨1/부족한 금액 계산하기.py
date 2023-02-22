def solution(price, money, count):
    answer = 0
    for i in range(1,count+1):
        answer += price*i
    
    if answer-money>0:
        return answer-money
    return 0

solution(3,20,4)

# count 만큼 반복 해서 price를 등차수열로 총 금액 계산
# 총금액 계산에서 있는돈 money를 빼서 리턴


"""
다른사람코드
    def solution(price, money, count):
        return max(0,price*(count+1)*count//2-money)

분석
    price*(count**2)+count//2 - money은 등차수열 공식
    max(0, 비용-소지금)은 소지금이 비용보다 큰 경우 음수가 나오기 때문에 0이 반환되는걸 이용

"""