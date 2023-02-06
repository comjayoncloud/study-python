def solution(sides):
    # 주어진 두변의 최대 길이의 변이 아닌 경우.
    #   가장 긴 변(주어지지 않는 변)의 길이는
    #   다른 두 변(주어진 두 변)의 길이의 합보자 작아야한다
    # unknown <sum(sides)

    #주어진 두 변 중에 최대 길이의 변이 없는 경우
    #   가장 긴 변(주어진 두변중 더 긴 변)의 길이는
    #   다른 두 변(주어진 두변중 더 짧은 변,주어지지 않는 변)의 길이의 합보다 작아야한다.
    # max(sides)<min(sides)+unknown
    # -> max(sides)-min(sides) < unknown  
    # -> max(sides)-min(sides) < unknown < sum(sides) 

    return sum(sides) - (max(sides)-min(sides)) - 1

solution([1,2])
solution([3,6])
solution([11,7])



"""
조건1. 받은 것중에 max가 가장 긴경우 max<n+min
6 <= n + 3 => n = 4,5,6 최대값은 max
11<= n + 7 => 5,6,7,8,9,10,11 최대값은 max
조건2. 나머지 입력되지 않은 값이 가장 긴경우
n<min+max

"""


"""
틀린이유 찾기
def solution(sides):
    answer = 0
    maxNumber = max(sides)
    minNumber = min(sides)
    for i in range(1,maxNumber):
        if (maxNumber<=i+minNumber):
            answer+=1
    for i in range(maxNumber,minNumber+maxNumber-1):
        if(i<minNumber+maxNumber):
            answer+=1
    print(answer)
    return answer
"""
