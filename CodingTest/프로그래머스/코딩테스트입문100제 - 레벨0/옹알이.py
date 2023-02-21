from itertools import permutations
def solution(babbling):
    answer = 0
    speek = ["aya","ye","woo","ma"]
    word = []
    for i in range(1, len(speek)+1):
        for j in permutations(speek, i):
            word.append(''.join(j))

    for i in babbling:
        if i in word:
            answer += 1

    return answer
    
solution(["aya", "yee", "u", "maa", "wyeoo"])


# "aya", "ye", "woo", "ma" 네가지 발음을 최대 한번씩 사용해 조합한 발음

