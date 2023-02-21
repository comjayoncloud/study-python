def solution(quiz):
    answer = []
    for i in quiz:
        a,b = map(str,i.split('='))
        
        if eval(a)==int(b):
            answer.append("O")
        else :
            answer.append("X")
        
    print(answer)
    return answer


solution(["3 - 4 = -3", "5 + 6 = 11"])	