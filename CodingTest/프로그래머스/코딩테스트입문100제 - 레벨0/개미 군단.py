def solution(hp):
    answer = 0
    
    while True:
        if hp==0:
            break
        elif hp>=5:
            answer += hp//5
            hp = hp - hp//5*5
        elif hp>=3:
            answer += hp//3
            hp = hp - hp//3*3
        elif hp >=1:
            answer += hp//1
            hp = hp - hp//1*1        

    return answer

solution(23)
solution(24)
solution(999)


"""
5 3 1 
최소한의병력-> 큰수부터 5->3->1
"""

"""
다른사람코드1
    def solution(hp):    
        return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)

다른사람코드2
    def solution(hp):
        answer = 0
        for ant in [5, 3, 1]:
            d, hp = divmod(hp, ant)
            answer += d
        return answer
"""