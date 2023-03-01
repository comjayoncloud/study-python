def solution(n, words):
    a = [1,2,3,4,5,6,7]
    
    for i in range(1,len(words)):
        
        print(words[:i])
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i%n)+1,(i//n)+1]
        else:
            return [0,0]

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	)
# solution(2,["hello", "one", "even", "never", "now", "world", "draw"]	)
# solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	)


"""

걸린시간 : 40분

생각한 해결방안 :
   
틀린점 :
    if , else , break 문으로 각각 다하려다보니.. 너무 복잡했다. 고로 다른사람 코드 참고하였음

다른사람코드 및 리뷰 :
    def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]
    => 파이썬 문법에 더 익숙해져야될듯하다.    
"""