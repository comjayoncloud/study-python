def solution(s):
    s_dict = {}
    answer=[]
    
    for i in range(len(s)):        
        #b 가없으면 answer -1
        if s[i] not in s_dict:
            answer.append(-1)
        else:
            answer.append(i-s_dict[s[i]])
        
        s_dict[s[i]]=i
        
    return answer

solution("banana")