"""
def solution(X, Y):
    answer = ''
    X,Y = sorted(list(X),reverse=True),sorted(list(Y),reverse=True)
    a = []
    for i in X:
        for j in Y:
            if i == j:
                if '0' in a:
                    continue
                else:
                    a.append(i)
                    X.pop(X.index(max(X)))
            else :
                continue
    
    if len(a) == 0:
        answer = "-1"
    else:
        answer = ''.join(a)
    return answer

solution("100","2345")
solution("5525","1255")
"""

# 입력값은 str , 출력값도 str
# 먼저 sort를 해줘서 내림차순으로 바꾼다.
# 같은 숫자가 없으면 -1
# 같은 숫자가 있으면 큰순서부터 뺀다.

def solution(X,Y):
    answer = []
    xDict = dict()
    yDict = dict()
    #x dict와 y dict에 키 밸류 선언
    for x in X:
        xDict[x] = xDict.get(x,0)+1
    for y in Y:
        yDict[y] = yDict.get(y,0)+1
 

    # xdict의 키를 ydict 키와 비교.있으면 밸류 -1씩 줄이고 answer 배열에 추가
    for key,val in xDict.items():
        if key in yDict.keys():
            while yDict[key]>0 and xDict[key]>0:
                    answer.append(key)
                    yDict[key]=yDict.get(key)-1     
                    xDict[key]=xDict.get(key)-1     

    # 아무것도 안들어왔을때!
    if len(answer)==0:
        return "-1"


    # 0은 한번만 사용해야함
    if(answer.count('0')==len(answer)): return "0"
    
    # 내림차순
    answer.sort(reverse=True)
    return ''.join(answer)

solution("100","2345")
solution("5525","1255")
