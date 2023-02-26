def solution(k, score):
    answer = []
    arr_k = []
    for i in range(len(score)):
        arr_k.append(score[i])
        arr_k.sort(reverse=True)
        if len(arr_k)>k:
            del arr_k[-1]
        answer.append(min(arr_k))

    return answer


solution(3,[10, 100, 20, 150, 1, 100, 200] )


# 1. k의 숫자로 유지할 배열의 길이를 구함
# 2. 빈 배열이 k 길이만큼 안나오면 쭉쭉넣음
# 3. sort를 하고 가장 작은 수 를 반환

6,7,8,12,19,21,22,23,26

"""
def solution(k, score):
    answer = []
    arr_k = []
    # score 길이만큼!
    for i in range(len(score)):
        #0~3일떄
        if len(arr_k)<k:
            arr_k.append(score[i])
            answer.append(min(arr_k))
        # 4 ~7 
        elif len(arr_k)==k:
            if score[i] >min(arr_k):
                arr_k.append(score[i])
                arr_k = sorted(arr_k,reverse=True)
                del arr_k[-1]
                answer.append(min(arr_k))
            elif score[i]<min(arr_k):
                answer.append(min(arr_k))
    return answer

    느낀점 :
        테스트 케이스에서 틀림.. ㅠ 
    """