def solution(numbers):
    answer = []
    for i in numbers:
        for j in numbers[1:]:
            if (i==j):
                continue
            else:
                answer.append(i*j)        
    a =max(answer)
    return a

def solution(numbers):
    numbers.sort(reverse = True)
    return max(numbers[0] * numbers[1],numbers[-1] * numbers[-2])



solution([1, 2, -3, 4, -5]	)