# import copy

# def solution(n, s):
#     answer = []
#     a = copy.deepcopy(s)-1
#     for i in range(1,s):
        
#         if i+a==s:
#             answer.append([i,a])
#         a-=1
#     print(answer)
#     return answer
# [[1, 7], [2, 6], [3, 5], [4, 4], [5, 3], [6, 2], [7, 1]]
# # solution(2,9) # 4,5
# # solution(2,1) # -1


def solution(n, s):
    if n > s:
        return [-1]
    
    p, q = divmod(s, n) 
    print(p,q)
    answer = [p] * n # [4,4]
    
    for i in range(q):
        answer[i] += 1
    print(sorted(answer))    
    return sorted(answer)
# solution(2,8) # 4,4
# solution(2,1) # -1
solution(2,9) # 4,5


"""

걸린시간 : 8시 49분 ~ 

생각한 해결방안 :
    n의 수만큼 s를 만드는 집합
    최고의 집합은 오름차순으로 정렬된 1차원 배열 (return)
    최고의 집합이 존재하지 않는 경우 -1 return

틀린점 :

다른사람코드 및 리뷰 :

"""

def solution(n, s):
    if n > s:
        return [-1]
    
    p, q = divmod(s, n)
    answer = [p] * n
    
    for i in range(q):
        answer[i] += 1
        
    return sorted(answer)