import numpy as np
def solution(num_list, n):
    a= (int(len(num_list)/n))
    answer = np.reshape(num_list,(a,n)).tolist()
    return answer

solution([1, 2, 3, 4, 5, 6, 7, 8],2)


"""
다른사람코드
    def solution(num_list, n):
        answer = []
        for i in range(0, len(num_list), n):
            answer.append(num_list[i:i+n])
        return answer
"""