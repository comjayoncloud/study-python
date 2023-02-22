def solution(numbers):
    answer = []
    for i in range(10):
        if i not in numbers:
            answer.append(i)
    
    return sum(answer)

solution([1,2,3,4,6,7,8,0])


"""
다른사람코드
    def solution(numbers):
        return 45 - sum(numbers)

분석
    0~9 까지라고 했기에... 0~9를 다더하면 45다. 이후 받은 배열의 합에서 빼면 간단함
    0~9 숫자를 봤을때 습관적으로 for이 먼저 생각났다. 다음번엔 경우의수를 더 생각해야겠다.       
"""