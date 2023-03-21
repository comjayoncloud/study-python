

from itertools import permutations
 
def check(unit, ban):
    for i in range(len(unit)):
        if len(unit[i]) != len(ban[i]): #가져온 tuple과 banned_id의 길이가 맞지않는다면 종료
            return False
        for j in range(len(unit[i])): #tuple의 스펠과 baaned_id가 맞지않는다면 종료, "*"는 그대로 진행
            if unit[i][j] != ban[i][j] and ban[i][j] != "*":
                return False
 
    return True
        
def solution(user_id, banned_id):
    answer = []
    print(list(permutations(user_id, len(banned_id))))
    for unit in permutations(user_id, len(banned_id)): #permutations에서 tuple을 한개씩 가져온다
        if check(unit, banned_id):
            if set(unit) not in answer: #겹치는지 판별
                answer.append(set(unit))
    
    return len(answer) #중복값이 제거된 answer의 길이출력


"""

걸린시간 : 1시간

초기 생각한 해결방안 :
    # 첫번쨰로 길이가 같아야되고
    # 두번째로 *를 제외한 나머지 자리가 같아야됌.

틀린점 및 느낀점 :
    permutations로 풀 생각 자체를 못했고 단순히 for으로만 사용하려했음..
    구글링 검색 후 여러 예제를 봤는데 , 나의 문제점은 함수하나 안에 모든걸 구현하려고해서 코드가 복잡해지는거 같음.




틀린코드 :
    # import re
    # def solution(user_id, banned_id):
    #     answer = 0
    #     for i in user_id:
    #         for j in banned_id:
    #             if len(i)==len(j):
    #                 a=[]
    #                 for y in range(len(i)):
                        
    #                     if i[y]==j[y]:
    #                         a.append("1")
    #                     elif i[y]!=j[y] and j[y]=="*":
    #                         a.append("2")
    #                     else:
    #                         a.append("0")
    #                 j = re.sub(r'[a-z]','1',j)
    #                 j = re.sub(r'[0-9]','1',j)
    #                 j =j.replace('*','2')
                    
    #                 if ''.join(a) ==j :
    #                     answer+=1
    #                     break



    #     print(answer)
            

    #     return answer
"""