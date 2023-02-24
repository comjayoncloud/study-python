def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
                    
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    
    return "".join(s)

# solution("AB",1)
solution("z",2)

"""
해결방안
    # chr,ord를 이용, s길이만큼 아웃풋
    1. z->a 일때 차이는 25 . 하지만 a->b 는 1차이.. 이 두개를 만족하는 공식을 구해야함
       z는 122 , a는 97. 알파뱃 개수는 총 26 
       %26으로 나누면 z는 18 , a는 19 ,b는 20 
       공식 = (받은문자 - a + 이동할만큼) % 26 + a
       
    1-1 대문자일때 is.upper()
    1-2 소문자일때 is.lower()
"""