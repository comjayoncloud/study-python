def solution(n, numlist):
    answer = []
    for i in numlist:
        if i%n==0:
            answer.append(i)
        else:
            continue

    return answer

solution(3,[4, 5, 6, 7, 8, 9, 10, 11, 12])


"""
다른사람코드
    def solution(n, numlist):
        return list(filter(lambda v: v%n==0, numlist))
    => filter! 다음엔 참고        

"""