"""
다른사람코드
    def solution(s):
        stack = []
        for num in s.split(' '):
            try:
                stack.append(int(num))
            except:
                stack.pop()
        return sum(stack)
"""


"""
해결방법
0. str에서 z를 0으로 바꾸자.
1. Z가 있으면 그앞전 숫자를 스킵하는 형태이니 , Z 가 있는지 확인하고 , 
2. Z가있으면 Z의 인덱스를 구하고 그앞 인덱스의 숫자를 0으로 바꾸고 sum으로 합을 구하면 될 거 같다.
3. Z가 없으면 그냥 sum 

import re
def solution(s):
    s = list(s)
    for i in s:
        if i =='Z':
            s[s.index('Z')] = "0"
    s = ''.join(s)
    numbers = list(map(int,re.findall("-?\d+", s)))   
    for i in numbers:
        print(i)
        if i == 0 :
            # print("헤헤")
            numbers[numbers.index(i)-1]= 0    
        else:
            continue
            # print(i)
    print(numbers)
    return sum(numbers)

-> 틀림... 아래 for i in numbers에서 한번만 실행하고 맘.. 왜 지 ??
"""





