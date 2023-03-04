def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        # capitalize 내장함수를 사용하면 첫 문자가 알파벳일 경우 대문자로 만들고
        # 두번째 문자부터는 자동으로 소문자로 만든다
        # 첫 문자가 알파벳이 아니면 그대로 리턴한다
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer

def solution(s):
    a = list(s.split())
    a = list(map(lambda x: x.lower(),a))
    for i in range(len(a)):
        a[i] = a[i].capitalize()

    return ' '.join(a)

solution("3people unFollowed me")
# solution("for the last week")


"""

걸린시간 : 10분

생각한 해결방안 :
    1. s를 띄워쓰기 기준으로 list로 받음
    2. 모두다 lower로 바꿈.
    3. capitalize()를 이용하여 맨앞만 대문자로 변환

틀린점 :
    def solution(s):
        a = list(s.split())
        a = list(map(lambda x: x.lower(),a))
        for i in range(len(a)):
            a[i] = a[i].capitalize()

        return ' '.join(a)
    공백문자로 이루어져 있음, 공백문자가 연속해서 나올수 있음의 조건을 생각하지 않았음.

다른사람코드 및 리뷰 :
    
"""