def solution(x):
    answer = []
    for i in str(x):
        answer.append(int(i))
    
    if x%sum(answer)==0:
        return True
    
    return False

solution(10)