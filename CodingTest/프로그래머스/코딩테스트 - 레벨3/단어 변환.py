from collections import deque
            #graph,node,visited
def solution(begin, target, words):
    count = 0 
    print([begin])
    for i in words:
        print(i[0])
        print(i[-1])
    
    return count
solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])


"""

걸린시간 : 

초기 생각한 해결방안 :
    1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
    2. words에 있는 단어로만 변환할 수 있습니다.
    3. 없으면 0 

    hot -> hit -> dot -> dog -> cog

틀린점 및 해결방안 :

다른사람코드 및 리뷰 :

"""

"""
from collections import deque


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    V = [ 0 for i in range(len(words))]
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break        
        for i in range(len(words)):
            temp_cnt = 0
            if not V[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    q.append([words[i], cnt+1])
                    V[i] = 1
                    
    return answer
"""