def solution(n, k):
    answer = 0
    if n>=10:
        k = k - (n // 10)
        answer = n * 12000 + k * 2000
    else : 
        answer = n * 12000 + k * 2000

    return answer

"""
다른사람
def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)
"""