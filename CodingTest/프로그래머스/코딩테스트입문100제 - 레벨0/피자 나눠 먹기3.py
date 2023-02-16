def solution(slice, n):
    result = 0
    while True:
        if result*slice >=n:
            break
        result +=1
    return result

# solution(7,10)
solution(4,12)


# n 명이 최소 한조각 이상 먹으려면?
# slice * result > n 


"""
다른사람풀이

    def solution(slice, n):
        return ((n - 1) // slice) + 1
"""