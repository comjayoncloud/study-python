def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i%divisor==0:
            answer.append(i)
    
    if len(answer)==0:
        answer.append(-1)
    else:
        answer = sorted(answer,reverse=False)

    return answer

solution([5, 9, 7, 10],5)

"""
다른사람코드
    def solution(arr, divisor): 
        return sorted([n for n in arr if n%divisor == 0]) or [-1]

    def solution(arr, divisor): 
        answer = sorted(list(filter(lambda x:x%divisor==0,arr))) or [-1]
        return answer

분석 및 느낀점
    list가 비어있으면 False. 오.. !!
"""