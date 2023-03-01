import re

def solution(s):
    # 반복횟수,제거된0의개수
    answer = [0,0]
    for i in range(len(s)):
        # A: 0이 있으면 answer [1]에 추가 후 0제거
        if '0' in s:
            answer[1]+=s.count("0")
            s = re.sub('0',"",s)
            # B,C : s의 길이를 2진수로 변환수 다시 str로 바꿈
            s = str(bin(len(s)))[2:]
            answer[0]+=1
        # 0이 없고 1만있을때?
        else:
            if s!="1":
                s = str(bin(len(s)))[2:]
                answer[0]+=1
            else:
                break
    return answer

solution("110010101001")

"""

걸린시간 : 23분

생각한 해결방안 :
    A. 문자열에 0이 있을때 , 1만있을때
        A-A-1 0이 있을때
        A-A-2 x의 모든 0 제거 => re.sub
        A-A-3 len(x) = c 
        A-A-4 c를 2진법 변환(문자열)

        A-B-1 1만있을때
        A-B-2 len(x)=c
        A-B-3 c를 2진법 변환(문자열)
    B. A 반복 , 받은 문자열이 1이되면 멈춤
    C. 아웃풋 (3반복한수 , 제거된0의개수 )

틀린점 :
    없음

다른사람코드 및 리뷰 :
    def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]

    => 사실 문제를 접근할때 이전에 푼 문제에서 replace는 효율성이 없다고 판단하여 문자열을 제거할 방법들을 찾아보았다.
       찾은 결과 방법은 strip,re.sub함수 였다. strip은 특성상 바깥쪽을 없애는것이기 때문에 코드가 복잡해지고 적합하지 않아
       보여 re.sub을 사용했었다. 또한 while문을 사용하면 메모리를 많이 잡아먹을거같아서 하지않았다.
       다른사람 코드에서 캐치한것은 , bin(정수) = str형태라는것. 고로 12줄에 있는 " s = str(bin(len(s)))[2:] "
       코드에서 str은 안 써도됨

"""