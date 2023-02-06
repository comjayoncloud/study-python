n = int(input())
a = []
if (1<=n<=30):
    for i in range(1,n+1):  
        if(i%10==3 or i%10 ==6 or i %10 ==9):
            a.append("X")
        else :
            a.append(i)
    print(*a)
else :
    print("1~30 숫자를 입력하세요")