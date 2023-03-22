def solution(citations):
    answer = 0
    a = sorted(citations,reverse=True)

    b=[]
    for i in range(1,len(citations)+1):
        print(i)
        count=0
        for j in a:
            # print(j)
            if j>=i:
                count+=1
        b.append(count)
    for i in range(len(b)):
        if b[i]<i:
            return i
    return answer

solution([3, 0, 6, 1, 5])

"""

걸린시간 : 7시 6분~

초기 생각한 해결방안 :

틀린점 및 해결방안 :

다른사람코드 및 리뷰 :

"""