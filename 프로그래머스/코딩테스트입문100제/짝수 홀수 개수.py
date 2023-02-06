def solution(num_list):
    answer = [0,0]
    for i in num_list:
        print(i)
        if i %2==0:
            answer[0] +=1
        else:
            answer[1] +=1
    print(answer)
    return answer

solution([1, 2, 3, 4, 5])


"""
다른사람 코드
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answe
"""