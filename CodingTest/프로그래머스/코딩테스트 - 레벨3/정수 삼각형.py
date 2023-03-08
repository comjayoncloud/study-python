from itertools import combinations

def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j==0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j]+= triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])

    return answer

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
"""
                                        a[0]  
                                a[0]+a[1][0] , a[0]+a[1][1]
                            a[0]+a[1][0]+a[2][0] , max(a[0]+a[1][1]


"""
"""

걸린시간 : 30분

초기 생각한 해결방안 :
    꼭대기 -> 바닥 숫자의 합이 가장 큰 경우찾기
    다음 배열은 처음과 끝은 정해져 있지만 겹치는 부분은 max로 처리해야됌.

틀린점 및 해결방안 :
    다른 사람 코드 인용

다른사람코드 및 리뷰 :

"""