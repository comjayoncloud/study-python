def solution(n):
    answer = 0 
    if (n%7==0):
        answer += n//7
    else :
        answer += (n//7)+1
    
    
    return answer

"""
다른사람

def solution(n):
    return (n - 1) // 7 + 1
"""