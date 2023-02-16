import re
def solution(my_string):
    answer = re.findall(r"[0-9]+",my_string)
    result = 0
    for i in answer:
        result += int(i)
    return result


solution("aAb1B2cC34oOp")


"""
다른사람코드
    def solution(my_string):
        s = ''.join(i if i.isdigit() else ' ' for i in my_string)
        return sum(int(i) for i in s.split())
"""