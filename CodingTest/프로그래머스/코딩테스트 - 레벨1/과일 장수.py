# def solution(k, m, score):
#     answer = 0
#     score.sort(reverse=True) #점수 내림차순 정렬
#     answer = sum([score[i+m-1] for i in range(0,len(score),m) if i+m <= len(score)])*m  
#     return answer
# solution(3,4,[1,2,3,1,2,3,1])

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True) 
    for i in range(0,len(score),m):
        if i+m<=len(score):
            answer += score[i+m-1]
            print(answer)
    answer = answer*m
    print(answer)
    return answer

solution(3,4,[1,2,3,1,2,3,1])




"""

def solution(k, m, score):
    answer = []
    score = sorted(score,reverse=False)
    
    price = 0
    #한번 돌때마다 1상자
    for _ in range(len(score)):
        if len(score)>=m:
            for _ in range(1,m+1):
                answer.append(max(score))
                # 뽑은 사과 배열에서 없애기.
                score.pop()
            # 가격 갱신 
            price += min(answer)*m*1
            
            # 한번 담은 answer 초기화
            answer=[]
        print(price)    
    return price
solution(3,4,[1,2,3,1,2,3,1])

def solution(k, m, score):
    answer = []
    score = sorted(score,reverse=False)
    
    price = 0
    #한번 돌때마다 1상자
    while len(score)>=m:
        for _ in range(1,m+1):
            answer.append(max(score))
            # 뽑은 사과 배열에서 없애기.
            score.pop()
        # 가격 갱신 
        price += min(answer)*m*1
        
        # 한번 담은 answer 초기화
        answer=[]
        
    return price

solution(3,4,[1,2,3,1,2,3,1])
# solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])


# => 시간초과.. while 문이라서 그런듯
"""