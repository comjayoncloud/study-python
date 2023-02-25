def solution(food):
    
    a = []
    # 2씩 나눔
    food = list(map(lambda x: x//2, food))
    food.pop(0)
    # print(food)
    for i in range(len(food)):
        
        if food[i]==0:
            continue
        else :
            # print(food.index(food[i]))
            for _ in range(1,food[i]+1):
                a.append(str(food.index(food[i])+1))
    b = list(reversed(a))
    c = ''.join(a)+"0"+''.join(b)
    print(c)
    return c

solution([1, 3, 2, 3])
"""
다른사람코드
    def solution(food):
        answer = ''
        for i in range(1,len(food)):
            answer += str(i)*(food[i]//2)
        temp = ''.join(reversed(list(answer)))
        return answer+'0'+temp

분석 및 느낀점
    내가만든 코드는 틀렸다.반례가 있었다.
    1. 같은 배열 안에 같은 원소가 있으면 기준을 앞으로만 둔다는것.
    -> 그래서 첫번째 원소(물)을 제거 햇음. 하지만 ,1,3,2,3 처럼 같은 원소 3 3이 오는경우
    -> 원하는 아웃풋 1230321 . 결과물 1110111

    다른사람코드처럼 깔끔하게 그냥 배열 이런거 상관없이 문자열로 바로바로 늘리는게 해결방법이였다..
"""

