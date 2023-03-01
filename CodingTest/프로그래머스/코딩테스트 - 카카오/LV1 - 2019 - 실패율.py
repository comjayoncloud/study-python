def solution(N, stages):
    answer = {}
    b = len(stages)
    #실패율을 인덱스와 함께 dictonary에 저장
    for i in range(1,N+1):
        if b!=0:
            answer[i] = (stages.count(i)/b)
            b -= stages.count(i)
        else:
            answer[i]=0
    # value 기준으로 내림차순(dict)
    
    c = dict(sorted(answer.items(), key = lambda item:item[1],reverse=True))
    
    # dict에서 키 만 list로 반환
    d = list(c.keys())
    

    return d


solution(5,[2, 1, 2, 6, 2, 4, 3, 3]) # 3 4 2 1 5

"""

걸린시간 : 7시 53분 ~ 8시 41분 

생각한 해결방안 :
    전체 스테이지수 N
    현재 멈춰있는 스테이지 번호
    실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

틀린점 :
    약 40~50분을 고민하닥다 풀었지만 런타임에러..

다른사람코드 및 리뷰 :
    def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

    => 나와 푼 방식이 비슷했다. 나의 코드에서 6,9,10 라인만 추가하니 됬다.
       0에 대한 예외 처리를 하니 런타임 에러에서 해결.. 도대체 왜 0에 대한 예외처리를 해야하는지..?
"""