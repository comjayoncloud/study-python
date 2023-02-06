n = int(input())

if (1<=n<=12):

    if n//3 == 1:
        print("spring")
    elif n//3 == 2:
        print("summer")
    elif n//3 == 3:
        print("fall")
    else:
        print("winter")
else:
    print("숫자를 다시입력하시오")