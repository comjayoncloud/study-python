import numpy as np
def solution(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist()

solution([[1,2],[2,3]],[[3,4],[5,6]])

"""
다른사람코드
    def sumMatrix(A,B):
        answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
        return answer

분석 및 느낀점
    zip만으로 해결하려했는데 생각보다 복잡해졌고 np를 사용하니 간단하게 풀렸다.
"""

