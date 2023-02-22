def solution(absolutes, signs):
    answer = []
    for i,j in zip(absolutes,signs):
        print(i,j)
        if j==True:
            answer.append(i)
        else:
            answer.append(-i)
    
    return sum(answer)


solution([4,7,12],[True,False,True])


"""
다른사람코드
    def solution(absolutes, signs):
        return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

분석
    짧지만.. 이해하기 좀 어려운거같다
"""