def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(max(array)))
    print(answer)
    return answer

solution([1, 8, 3])