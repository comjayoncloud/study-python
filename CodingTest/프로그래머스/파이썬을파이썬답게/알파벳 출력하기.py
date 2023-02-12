num = int(input().strip())
answer ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if num == 0:
    print(answer.lower())
elif num == 1:
    print(answer.upper())

# str의 메소드 lower,upper


"""
import string
string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789
"""