def solution(a, b, n):
    answer = 0
    # 단, 보유 중인 빈 병이 2개 미만이면, 콜라를 받을 수 없다.
    # 빈 병의 개수가 콜라를 받기 위해서 필요한 개수보다 크면 반복한다
    while (n >= a):
        remain_bottle = n % a
        n = (n//a) * b # 마트에서 받은 콜라의 수
        answer += n # 받은 걸 answer에 +
        n += remain_bottle # 남아있는 병을 더해줘서 다음에 마트갈 때 이용
    return answer

solution(2,1,20)
# solution(3,1,20)


# a는 빈병 몇개 필요한지 , b는 a만족후 받을 콜라 개수 , n은 빈 병
# result는 콜라 개수
# 단, 보유 중인 빈 병(n)이 2개 미만이면, 콜라를 받을 수 없다.


"""
다른사람코드
    solution = lambda a, b, n: max(n - b, 0) // (a - b) * b

분석
    한꺼번에 계산하지 않고 a개만 팔고 b개를 받는 과정은 결국 a-b 개씩 병을 소비하는 것으로 생각, 
    첫번째 진행할 때는 a개만 소비되기 때문에, b만큼 못받음(-b), 
    그 조건을 먼저 계산 n-b 반복횟수는 n-b // (a-b) 여기에 받는 병수 b 곱한 것 .. 이렇게 풀수도 있군요 ㅎㅎ
"""