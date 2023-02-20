def solution(lines):
    answer = 0
    for i in range(3):
        l1,l2 = lines[i-1],lines[i]
        print(l1,l2)
    return answer

solution( [[0, 2], [-3, -1], [-2, 1]])
# solution([[0, 1], [2, 5], [3, 9]])

# 첫번째 배열 = 오른쪽 아래선
# 두번째 배열 = 왼쪽 아래선
# 세번재 배열 = 위쪽 선



# 다시풀기