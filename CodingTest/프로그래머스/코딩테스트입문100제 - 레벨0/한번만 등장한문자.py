from collections import Counter


def solution(s):
    answer = []
    a = dict(Counter(s))
    print(Counter(s))
    for i in a:
        if a[i] == 1:
            answer.append(i)
    # print(type(a))
    answer = sorted(answer,reverse=False)    
    return ''.join(answer)

solution("abcabcadc")


# str 을 리스트로 하나씩 비교하자 . counter 사용하면 될듯


"""
다른사람코드1
    def solution(s):
        answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
        return answer

"""