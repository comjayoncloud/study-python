n = int(input())
if (0<=n<=100):
    if(90<=n):
        print("A")
    elif(70<=n<=89):
        print("B")
    elif(40<=n<=69):
        print("C")
    elif(0<=n<=39):
        print("D")
else: 
    print("숫자를 다시입력하세요. 0~100")