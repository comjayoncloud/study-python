
a,b = map(int,input().split())
if (-2147483648 <= a)and(b <= +2147483647):
    if (a<=b):
        print(True)
    else:
        print(False)
else:
    print("다시입력하세요")

    