def solution(answers):
    answer = []
    a1 = [1, 2, 3, 4, 5] # 1번째 수포자의 답을 넣은 리스트
    a2 = [2, 1, 2, 3, 2, 4, 2, 5] # 2번째 수포자의 답을 넣은 리스트
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    print(a1[0%5])
    print(a1[1%5])
    return answer

solution([1,2,3,4,5])