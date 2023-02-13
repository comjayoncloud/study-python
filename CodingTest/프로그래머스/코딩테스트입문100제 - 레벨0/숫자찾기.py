def solution(num, k):
    a,b = map(str,(num,k))
    for i in range(len(a)):
        if b in a:
            return a.find(b)+1
        else:
            return -1
    return 


solution(29183,5)


"""
다른사람코드1 :
    def solution(num, k):
        for i, n in enumerate(str(num)):
            if str(k) == n:
                return i + 1
        return -1

다른사람코드2 :
    def solution(num, k):
        return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1
"""