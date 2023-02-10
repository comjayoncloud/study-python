def solution(array,commands):
    
    answer = []
    # 코맨드 길이만큼 반복.
    for i in range(len(commands)):
        a = array[commands[i][0]-1:commands[i][1]]
        b =sorted(a,reverse=False)
        answer.append(b[commands[i][2]-1])
    return answer

solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])	




"""
다른사람코드
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


다른사람코드2
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

다른사람코드3

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer
"""

"""
느낀점 :
    다른사람들 코드들 보면서 좀더 간소화하고 가독성 좋게 만들수 있도록 해야겠다.
"""