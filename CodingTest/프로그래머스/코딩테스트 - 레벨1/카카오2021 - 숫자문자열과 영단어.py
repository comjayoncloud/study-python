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
    2. 딕셔너리 만들음. {영문자:숫자}
    3. s안에 영문자가 있으면 딕셔너리를 이용하여 숫자로 바꿈
    4. 아웃풋은 int 이기에 str를 int로 바꿈
"""