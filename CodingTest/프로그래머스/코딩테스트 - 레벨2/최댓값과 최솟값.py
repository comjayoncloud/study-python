def solution(s):
    answer = ''
    

    a = list(map(int,s.split()))
    
    b = min(a)
    c = max(a)
    
    d = f'{str(b)} {str(c)}'
    print(d)
    return d

solution("1 2 3 4")

"""
생각한 해결방안 : 
    1. a 배열 생성 후 s를 for문으로 a배열에 넣는데 ' '를 제외하고 int 형태로 바꿈 (split.(), map)
    2. min , max 를 이용하여 리턴 

틀린점 :
    없음

다른사람코드 및 리뷰 :
    def solution(s):
        s = list(map(int,s.split()))
        return str(min(s)) + " " + str(max(s))
    
    => 

걸린시간 : 10분
"""
