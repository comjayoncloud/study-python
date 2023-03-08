# C 해결법
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

"""
A 해결법 -> 코드 실행 성공 , 테스트 케이스 3~12 실패
반례: [1,2,1,2,3,1,3,1,2,3,1,2,3,1]

def solution(ingredient):
    answer = 0
    hamburger = [1,2,3,1]
    a=0
    for _ in range(len(ingredient)):
        print(ingredient)
        if ingredient[a:a+4:] == hamburger:
            answer+=1
            del ingredient[a:a+4]
            # print(ingredient)
            a=0
        else:
            a+=1    
    # print(answer)
    return answer

solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
# solution([1,2,1,2,3,1,3,1,2,3,1,2,3,1])


-----------------------------------------------------------------------------


B 해결법 -> 코드 실행성공, 테스트케이스 시간초과
def solution(ingredient):
    answer =0
    ingredient = ''.join(map(str,ingredient))
    
    for i in range(len(ingredient)//2):
        if '1231' in ingredient:
            answer+=1
            ingredient = ingredient.replace('1231','',1)
    return answer

solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
"""

"""

걸린시간 : A-18분 B-10분 C-5분

초기 생각한 해결방안 :
    #빵1 - 야채2 - 고기3 - 빵1
    1-2-3-1
    받은 재료에서 햄버거 몇개인지?
    순서 중요함. sort x

    A. 배열로 해결
    1. ingredient len 만큼 반복
    2. hamburger 조합인 1231 배열선언
    3. ingredient 배열을 슬라이싱으로 hamburger 배열과 비교 . 조건이 성립하면 count +=1 , ingredient 원소 없앰
    
    B. 문자열로 해결
    1. replace로 해결

    C. 배열 + pop

틀린점 및 해결방안 :
    A 방법은 테스트케이스 에서 실패한이유가 뭘까.. 반례를 못찾겠음.
    B 문자열은 시간초과
    C 는 배열이용하였고 del 대신 pop사용

다른사람코드 및 리뷰 :
    정답인 C를 다른사람 코드를 참고하였는데.. 왜 del이었을땐 안되고 pop은 잘되는지... 
    이해가 잘안됀다.

"""