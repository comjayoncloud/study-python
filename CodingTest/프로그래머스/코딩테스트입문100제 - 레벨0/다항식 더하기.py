def solution(polynomial):
    # 1. + 기준으로 나누기
    a = polynomial.replace(' ','').split('+')
    
    # 2. x만들어있는 b 배열과 a배열에서 pop
    b = []
    for i in range(len(a)):
        # x가 있는지 확인
        if 'x' in a[i]:
            #있을때 그냥 x면 b에 1 추가, 아니면 x빼고 b에 추가
            if a[i]=='x':
                b.append(int(1))   
                a[i]=0
            else:
                b.append(int(a[i].replace('x','')))
                a[i]=0
    # 계산을위해 a의 요소들 int로 형변환
    a = list(map(int,a))

    #결과값 c만들기
    if sum(a)==0:
        if sum(b)==1:
            c="x"
        else:
            c = f"{sum(b)}x"
    elif sum(b)==0:
        c = f"{sum(a)}"
    else:
        if sum(b)==1:
            c =f"x + {sum(a)}"
        else:
            c = f"{sum(b)}x + {sum(a)}"
    return c

# solution("3x + 7 + x")
solution("x + x + x")
"""
# x만존재 -> x 기준으로 나누기
# 0~9 , x , + 로 이뤄져있음 -> + 기준으로 나누기

# 1. +로 기준나누기
# 2. x만 가지고 있을 배열 . 1x는 없음.
# 3. 결과값 c 만들기.
"""


"""
다른사람 코드
def solution(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'
"""