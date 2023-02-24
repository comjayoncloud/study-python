from itertools import combinations

def solution(numbers):
    answer = []
    numbers = sorted(combinations(numbers,2),reverse=False)
    for i in range(len(numbers)):
        if answer[i]==sum(numbers[i]):
            continue
        answer.append(sum(numbers[i]))


    
    return answer

solution([2,1,3,4,1])