def solution(mylist):
    answer = list(map(lambda x:len(x), mylist))
    print(answer)
    return answer

solution([[1], [2]])