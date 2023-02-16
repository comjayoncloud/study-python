
def solution(array, n):
    answer =[]
    for i in array:
        answer.append(abs(i-n))
    return array[answer.index(min(answer))]

solution([3, 10, 28],20)
solution([10, 11, 12],13)


"""
# 배열과 n을 받음.
# 배열 원소 중에 n과 가장 가까운수를 찾자
# 1. 받은 배열 a와 n을 - 해서 값의 절대값 차이를 구해서 새로운 배열 b에 넣음
# 2. b 배열에서 가장 작은 값 min의 인덱스를 찾자.
# 3. 리턴값으로 a의 인덱스  
"""

"""
다른사람코드
    def solution(array: list, n: int) -> int:
        return array[sorted([[index, abs(n-num), num] for index, num in enumerate(array)], key=lambda x: (x[1], x[-1]))[0][0]]

다른사람코드2
    solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

"""