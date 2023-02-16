def solution(my_str, n):    
    result = [my_str[i * n:(i + 1) * n] for i in range((len(my_str) + n - 1) // n )] 
    return result

solution("abc1Addfggg4556b",6)



"""
다른사람코드
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]

    -> 슬라이싱은 인덱스가 len을 초과해도 에러가 나지 않는다..
"""