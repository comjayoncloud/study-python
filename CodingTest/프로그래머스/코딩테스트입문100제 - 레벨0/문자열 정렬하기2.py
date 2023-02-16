def solution(my_string):
    return ''.join(sorted(my_string.lower(),reverse=False))

solution("Bcad")
solution("heLLo")
solution("Python")

"""
# 모두 소문자로 변환 -> lower()
# 알파벳 순서대로 정렬 -> sorted
"""


"""
다른사람코드
    def solution(my_string):
        answer = []
        for i in my_string:
            if ord(i) >= ord('A') and ord(i) <= ord('Z'):
                answer.append(chr(ord(i)+32))
            else:
                answer.append(i)
        return ''.join(sorted(answer))
"""