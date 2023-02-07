def solution(n):
    a = str(n)
    
    b = []
    for i in range(len(a)):
        b.append(int(a[i]))
    answer = sum(b)
    print(answer)

    return answer

solution(int(123))