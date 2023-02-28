def solution(brown, yellow):
    answer = []
    total = brown + yellow                  # a * b = total

    for b in range(1,total+1):
        if (total / b) % 1 == 0:            # total / b = a
            a = total / b
            print(a,b)
            if a >= b:                      # a >= b
                if 2*a + 2*b == brown + 4:  # 2*a + 2*b = brown + 4 
                    return [a,b]
    return answer

solution(10,2)
"""

걸린시간 : 1시간

생각한 해결방안 :
    A
    전체카펫의 크기는 기억하지못함, 가로길이는 세로 길이와 같거나 김
    10 2 = 12 -> 4 ,3 => 1 2 3 4 6 12
    8 1 = 9 -> 3,3 => 1 3 3 9 
    24 24 = 48 -> 1 2 3 4 6 8 12 16 24 48
    1. 전체 크기는 brown+yellow
    2. 약수에서 가장 가운데 숫자의 앞 뒤를 바꿔서 도출하면됨.
    => 시간초과
    
    B
    a는 가로 b는 세로일떄
    1. a>=b
    2. 2a+2b -4 = brown => 2a+2b = brown +4
    3. (a-2) * (b-2) = yellow => ab -2a -2b +4 = yellow

    4. 2와 3의 조건을 같이 정리하면 .. ab -(brown +4) +4 = yellow
    5. ab = yellow + brown
    
틀린점 :
    A밖에 생각을 못함..
다른사람코드 및 리뷰 :
    정답이 다른사람 코드이다.. 수학적 접근을 하였는데, 와 이걸어떻게 생각한건지... 대단하다.
"""

# def solution(brown, yellow):
#     answer = []
#     size = brown+yellow
#     for i in range(1,size+1):
#         for j in range(size+1,1,-1):
#             if i*j == size:
#                 answer.append([j,i])

#     return answer[len(answer)//2]