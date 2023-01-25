n = int(input())
s = 0
if (0<=n<=100):
    for i in range(n+1):
        if(i%2==0):
            s += i
    print(s)

else:
    print("0~100 숫자를 입력하시오")