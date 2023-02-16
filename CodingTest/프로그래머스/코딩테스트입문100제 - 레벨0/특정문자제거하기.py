def solution(my_string, letter):
    answer = list(my_string)
    for i in answer:
        if i == letter:
            answer.pop(answer.index(i))
    return ''.join(answer)

solution("abcdef","f")

"""
다른사람코드
    def solution(my_string, letter):
        return my_string.replace(letter, '')

"""