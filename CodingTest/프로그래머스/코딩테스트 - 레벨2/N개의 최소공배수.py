import math

def solution(arr):
    answer = arr[0]
    for num in arr:                                 # 반복문을 처음부터 끝까지 돈다.
        #1. (arr[0],arr[1])의 최소공배수를 구한 후 answer에 저장
        #2. (#1에서 구한 최소공배수, arr[2])의 최소공배수를 구한 후 answer에 저장
        #3. 모든 배열을 돌면서 최소공배수를 구하고, 저장하고 하는 방식을 진행
        answer = answer*num // math.gcd(answer, num)
    return answer

solution([2,6,8,14]	)

"""

걸린시간 : 5분

초기 생각한 해결방안 :
    두 수의 배수 중 공통이 되는 가장 작은 숫자. 2, 7 최소 공배수는 14
    n개 공배수를 치니 python 3.9부터 math gcd를 이용해서 공배수를 구할수 있음.
    첫번째 원소 지정후 그다음부터 그다음 숫까지 포함한 공배수를 계속해서 구함.
    gcd 는 두수의 최대 공약수를 구해주는 함수.
    최소공배수 = (x*y) / gcd(x,y)

틀린점 및 해결방안 :

다른사람코드 및 리뷰 :

"""