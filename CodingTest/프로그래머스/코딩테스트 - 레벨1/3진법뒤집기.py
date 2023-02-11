def solution(n):
    
    rev_base=''
    while n >0:
        n,mod = divmod(n,3)
        rev_base += str(mod)
    return int(rev_base,3)

solution(45)


"""
다른사람코드
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
"""