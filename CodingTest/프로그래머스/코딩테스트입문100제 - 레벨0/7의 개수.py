def solution(array):
    answer = []

    for i in map(str,array):
        answer.append(i.count('7'))
       
    return sum(answer)

solution([7, 77, 17])


"""
다른사람코드1
    def solution(array):
        return str(array).count('7')
"""