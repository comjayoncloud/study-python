def solution(ingredient):
    answer = 0
    a = list(map(str,ingredient))
    b = ''.join(a)
    
    for i in b:
        if '1231' in b:
            answer+=1
            b = b.replace('1231','')
            print('o')
            
    return answer

solution([2, 1, 1, 2, 3, 1, 2, 3, 1])

#-> 시간초과로 오류가남..


"""
순서: 빵-야채-고기-빵
=> 1 2 3 1 
1 - 빵
2 - 야채
3 - 고기
"""


def solution(ingredient):
    answer = 0
    
    stack=[]
    for i in ingredient:
        stack.append(i)
        if stack[-4:]==[1,2,3,1]:
            answer+=1
            for k in range(4):
                stack.pop()
            
    return answer