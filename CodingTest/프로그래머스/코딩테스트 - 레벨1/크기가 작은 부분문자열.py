def solution(t, p):
    count = 0 

    for i in range(len(t)):
        a = t[i:i+len(p)]
        print(a)
        if len(a) == len(p) and int(a)<=int(p):
            count+=1

    return count

solution("3141592","271")
# solution("500220839878","7")
# solution("10203","15")


# 1. 길이가 같아야됨
# 2. 길이가 같을때 p와 비교

"""
다른사람코드1
    def solution(t, p):
        answer = 0

        for i in range(len(t) - len(p) + 1):
            if int(p) >= int(t[i:i+len(p)]):
                answer += 1

        return answer

분석
    len(t)-len(p)+1 은 p의 길이만큼 t에서 만들수 있는 조합의 경우의수다
    t[i:i+len(p)]는 비교할 수들
"""