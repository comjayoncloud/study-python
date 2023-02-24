def solution(d, budget):
    answer = 0
    d = sorted(d,reverse=False)
    for i in range(len(d)):
        if budget >= d[i]:
            budget -= d[i]
            answer +=1
    print(answer)
    return answer

solution([1,3,2,5,4],9) # 1 3 5
# solution([2,2,3,3],10) # 2 2 3 3 


"""
다른사람코드
    def solution(d, budget):
        d.sort()
        while budget < sum(d):
            d.pop()
        return len(d)
"""