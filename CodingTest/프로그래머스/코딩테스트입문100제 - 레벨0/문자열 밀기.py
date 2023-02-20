import copy

def solution(A, B):
    C=[]
    result = 0
    # 배열 길이만큼 밀어보고 if 조건에 맞으면 1 아니면 -1
    for i in range(len(A)):
        if A==B:
            return 0
        else :
            print(A[-1])
            C.append(A[-1])
            C += A[0:-1]
            print(C)
            result +=1
            if(''.join(C) == B):
                return result
            else :
                A = copy.deepcopy(C)
                C.clear()
        
    return -1

solution("apple","elppa")


"""
다른사람코드1
    solution=lambda a,b:(b*2).find(a)

다른사람코드2
    def solution(A, B):
        #if A == "":
        #    return 0

        AA = A+A
        answer = AA.find(B)

        if answer >0:
            answer = len(A) - answer

        return answer
"""