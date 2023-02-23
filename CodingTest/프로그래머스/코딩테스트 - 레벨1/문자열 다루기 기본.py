def solution(s):
    print(s.isdecimal())
    if len(s)==4 or len(s)==6 :
        if s.isdecimal() ==False:
            return False
        elif s.isdecimal()==True:
            return True
    return False

solution("aaaa") # false
solution("1234") # true
solution("a234") # false



"""
다른사람코드
    def alpha_string46(s):
        return s.isdigit() and len(s) in [4,6]

분석 및 느낀점
    les(s) in [4,6] 은 4~6이 아닌 4또는 6
"""