def solution(participant, completion):
    # 1. 두 list를 sorting한다
    participant.sort()
    completion.sort()

    # 2. completeion list의 len만큼 participant를 찾아서 없는 사람을 찾는다
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]

    # 3. 전부 다 돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수이다.
    return participant[len(participant)-1]

solution(["leo", "kiki", "eden"],["eden", "kiki"])

"""

걸린시간 : 6시29분 ~ 7시 4분

생각한 해결방안 :
    A. sort
    B. 있는지 없는지 비교 .
    C. 다돌아도 없을경우 마지막 주자가 완주
틀린점 :

다른사람코드 및 리뷰 :
    def solution(participant, completion):
        hashDict = {}
        sumHash = 0
        
        # 1. Hash : Participant의 dictionary 만들기
        # 2. Participant의 sum(hash) 구하기
        for part in participant:
            hashDict[hash(part)] = part
            sumHash += hash(part)
        
        # 3. completion의 sum(hash) 빼기
        for comp in completion:
            sumHash -= hash(comp)
        
        # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다

        return hashDict[sumHash]

"""