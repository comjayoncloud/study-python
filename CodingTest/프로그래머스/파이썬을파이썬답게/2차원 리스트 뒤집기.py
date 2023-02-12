def solution(mylist):
    answer = list(map(list,zip(*mylist)))


    return answer

solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# zip 함수..!!