import numpy
def solution(score):
    avg_score = []
    answer = []
    for i in score:
        avg_score.append((numpy.mean(i)))
    
    #내림차순
    sort_avg_score = sorted(avg_score,reverse=True)

    for i in avg_score:
        answer.append(sort_avg_score.index(i)+1)

    
    return answer

# solution([[80, 70], [90, 50], [40, 70], [50, 80]]) 
solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]])

"""
1. 영어점수,수학점수의 평균값으로 등수 매김 - 평균값 : numpy
2. 점수가 같으면 중복 등수 가능 .중복 등수가 있으면 다음 등수는 없음 

느낀점 : 파이썬의 index함수는 같은 값이 있을경우 더 앞의 값을 리턴해줌..
"""

"""
다른사람코드
    def solution(score):
        a = sorted([sum(i) for i in score], reverse = True)
        return [a.index(sum(i))+1 for i in score]
"""