def solution(numbers):
    numbers = sorted(numbers,reverse=True)    
   
    return numbers[0]*numbers[1]

solution([1, 2, 3, 4, 5])

# 원소중 두개 곱해서 만들수 있는 최댓값

"""
다른사람 코드

    def solution(numbers):
        numbers.sort()
        return numbers[-2] * numbers[-1]
"""