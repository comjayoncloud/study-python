def solution(s):
    answer = ''
    print(sorted(s,reverse=True))
    return ''.join(sorted(s,reverse=True))

solution("Zbcdefg")