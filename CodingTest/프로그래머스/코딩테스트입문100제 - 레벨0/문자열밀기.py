def solution(A, B):
    if A==B:
        return 0
    else:
        C =[]
        C.append(A[-1])
        C += A[0:-1]
        answer = ''.join(C)
        if answer ==B:
            return 1
        else : 
            return -1
    
    return 0

solution("hello","ohell")