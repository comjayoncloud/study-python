def solution(n, arr1, arr2):
    answer = []


    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        print(tmp)
        tmp = tmp[2:].zfill(n)
        tmp = tmp.replace('1','#').replace('0',' ')
        answer.append(tmp)
    print(answer)

    return answer

solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])
"""

걸린시간 : 29분

생각한 해결방안 :
    각 배열의 원소 x를 2진수로 변환했을때 길이는 n 이하
    0 <= x <= 2*n-1
    아웃풋은 # ,공백으로 구성된 문자열 출력

    1. or 을 사용하여 0,1 둘중에 하나만 있을때 1 을반환하는 것을 사용
    2. bin을 사용하면 앞에 0b가 붙기에 슬라이싱으로 없애기
    3. replace 사용하여 1,0을 바꾸고 answer배열에 추가

틀린점 :
    없음

다른사람코드 및 리뷰 :
    def solution(n, arr1, arr2):
        answer = []
        for i,j in zip(arr1,arr2):
            a12 = str(bin(i|j)[2:])
            a12=a12.rjust(n,'0')
            a12=a12.replace('1','#')
            a12=a12.replace('0',' ')
            answer.append(a12)
        return answer
    => zfill 대신 rjust 사용 , zip 함수 사용

"""

