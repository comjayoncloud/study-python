#2번째로 푼방법 count 사용
def solution(i,j,k):
    count = 0
    for a in range(i,j+1):
        count +=(str(a).count(str(k)))
    return count
solution(1,13,1)
"""
#첫번째로 푼방법 
def solution(i, j, k):
    count = 0
    b = []
    for a in range(i,j+1):
        b.append(list(str(a)))
    c = sum(b,[])
    
    for i in c :
        if(str(k) in i):
            count+=1
    return count
"""


# def solution(i, j, k):
#     answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
#     return answer



"""
느낀점 :
    내가 처음 푼 방법으로는 답은 맞지만 시간초과가.. 났다
    count를 사용하는 방법이 있었다.
"""

