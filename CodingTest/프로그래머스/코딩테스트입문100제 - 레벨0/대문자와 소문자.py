def solution(my_string):
    answer=[]

    for i in my_string:
        print(i.isupper())
        if i.isupper()==True:
            answer.append(i.lower())
        else:
            answer.append(i.upper())

    return ''.join(answer)



solution("cccCCC")


"""
다른사람코드1
    def solution(my_string):
        return my_string.swapcase()

다른사람코드2
    def solution(my_string):
        answer = ''

        for i in my_string:
            if i.isupper():
                answer+=i.lower()
            else:
                answer+=i.upper()
        return answer
"""