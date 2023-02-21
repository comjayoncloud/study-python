def solution(my_string):
    char_remov= ['a','e','i','o','u']
    for char in char_remov:
        my_string = my_string.replace(char, '')
    return my_string
solution("bus")


# def solution(rsp):
#     d = {'0':'5','2':'0','5':'2'}
#     return ''.join(d[i] for i in rsp)
