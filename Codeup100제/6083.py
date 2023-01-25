r,g,b = map(int,input().split())
count = 0
if (1<=r,g,b<=3):
    for i in range(r):
        for j in range(g):
            for k in range(b):
                print(i,j,k)
                count +=1
    print (count)
else:
    print("숫자를 다시입력하셈")