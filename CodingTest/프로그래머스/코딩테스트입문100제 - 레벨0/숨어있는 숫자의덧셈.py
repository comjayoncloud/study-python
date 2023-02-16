import re

def solution(my_string):
    answer = re.findall('\d',my_string)
    result = 0
    print(answer)
    for i in answer:
        result += int(i)
    return result


solution("aAb1B2cC34oOp")



"""
다른사람코드
    def solution(my_string):
        return sum(int(i) for i in my_string if i.isdigit())

코드2
    import re
    def solution(my_string):
        return sum(int(n) for n in re.sub('[^1-9]', '', my_string))
"""