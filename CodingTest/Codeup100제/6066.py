a,b,c = map(int,input().split())
if (0<=a and b and c <=2147483647):
    if (a%2==0) :
        print("even")
    else :
        print("odd")
    if b%2==0:
        print("even")
    else:
        print("odd")
    if c%2==0:
        print("even")
    else:
        print("odd")
else:
    print("숫자를 다시 입력하세요")