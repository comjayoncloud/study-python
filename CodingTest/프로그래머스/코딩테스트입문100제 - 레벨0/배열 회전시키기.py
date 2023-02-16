import copy

def solution(numbers, direction):

    if direction=="right":
        answer = [numbers[-1]]+numbers[:len(numbers)-1]
        
    elif direction=="left":
        answer = numbers[1:]+[numbers[0]]

    return answer
    

solution([1, 2, 3],"right")

# right 일때 마지막 숫자가 첫번째로 온다.

# left 일때는 처음숫자가 마지막으로 간다.


"""
다른사람코드

    from collections import deque

    def solution(numbers, direction):
        numbers = deque(numbers)
        if direction == 'right':
            numbers.rotate(1)
        else:
            numbers.rotate(-1)
        return list(numbers)
"""