def solution(mylist):
    answer =[]
    for i in range(len(mylist)):
        if i == (len(mylist)-1):
            break
        else:
            answer.append(abs(mylist[i+1]-mylist[i]))

    return answer

solution([83, 48, 13, 4, 71, 11])

# 출력 :[35, 35, 9, 67, 60]


def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

"""
원하는 답은 zip함수를 쓰는것이다..! zip을 사용하면 index를 사용하지않고
각 원소에 접근할 수 있다!!
"""