def solution(s):
    answer =''
    
    alphabet_dict ={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    for key,value in enumerate(alphabet_dict):
        print(key,value)
        if value in s:
            s=s.replace(value,str(key))
        answer=s

    return int(answer)


solution("one4seveneight")

"""
제한시간 : 10분 7시53분~ 

해결방안 :
    1. 인풋(영어+숫자) -> 아웃풋(숫자)

"""