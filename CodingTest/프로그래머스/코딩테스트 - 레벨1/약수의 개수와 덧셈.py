def solution(left, right):
    count =0
    answer=[]
    # left~right
    for i in range(left,right+1):
        #약수의 개수 구하기
        for j in range(1,i+1):
            if i%j==0:
                count +=1
        #약수의 개수를 기준으로 짝,홀 구분해서 배열에 추가
        if count %2==0:
            answer.append(i)
            count=0
        else:
            answer.append(-i)
            count=0
    return sum(answer)

solution(13,17)


"""
다른사람코드
    def solution(left, right):
        answer = 0
        for i in range(left,right+1):
            if int(i**0.5)==i**0.5:
                answer -= i
            else:
                answer += i
        return answer

분석 
    제곱수의 약수는 홀수개
    제곱수를 제외한 모든 정수들의 약수의 개수는 무조건 짝수 개수이며 제곱수만 홀수 개수임을 알았으면 
    이렇게 풀 수 있군요.. 수학적 사고... 수학적 사고...



"""