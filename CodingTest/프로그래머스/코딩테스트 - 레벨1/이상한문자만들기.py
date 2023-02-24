def solution(s):
    answer = list(s.split())
    a = ''
    for i in answer:
        for j in i:
            print(i.index(j))
            if i.index(j)%2==0:
                # print(j)
                a+= (j.upper())
            elif i.index(j)%2==1:
                # print(j)
                a+=(j.lower())                
        a+=' '    
    print(a)
    return a

solution("try hello world")

#짝수 = 대문자
#홀수 = 소문자


"""

    def solution(s):
        answer = ''
        new_list = s.split(' ')
        for i in new_list:
            for j in range(len(i)):
                if j % 2 == 0:
                    answer += i[j].upper()
                else:
                    answer += i[j].lower()
            answer+= ' '
        return answer[0:-1]
        
    """