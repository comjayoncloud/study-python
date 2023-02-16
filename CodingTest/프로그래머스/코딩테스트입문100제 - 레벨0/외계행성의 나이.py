def solution(age):
    answer = []
    for i in str(age):
        answer.append(chr(int(i)+97))
    return ''.join(answer)

solution(23)


"""
다른사람코드
def solution(age):

    return ''.join([chr(int(i)+97) for i in str(age)])
"""