def solution(num):
    answer = 0
    a =0
    while a<500:
        a+=1
        if num ==1:
            return answer
        elif num%2==0:
            num =num/2
            answer +=1
        else:
            num =num*3+1
            answer+=1
    return -1

solution(6)
solution(16)


"""
다른사람코드
    def collatz(num):
        for i in range(500):
            num=num/2 if num%2==0 else num*3+1
            if num==1:
                return i+1
        return -1

분석 및 느낀점:
    for문은 너무 진부해서 while로 풀엇다
"""