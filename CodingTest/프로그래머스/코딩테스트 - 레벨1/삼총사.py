from itertools import combinations


def solution(number):
    count = 0
    a = list((combinations(number,3)))
    for i in a:
        if sum(i)==0:
            count +=1
    
    return count

solution([-2, 3, 0, 2, -5])

"""
해결방안
1. combination 사용해서 3개씩 모든 조합을 리스트로 만든다.
2. 리스트를 for문을 사용해서 각 원소에 접근한후 sum을 이용해서 0과 같으면 count를 1씩 증가시킨다.

다른사람코드
    def solution (number) :
        from itertools import combinations
        cnt = 0
        for i in combinations(number,3) :
            if sum(i) == 0 :
                cnt += 1
        return cnt

분석
    다른점은 for 문 안에서 콤비네이션을 그냥 썻다는 차이점정도.    
"""