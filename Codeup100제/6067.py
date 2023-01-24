# 숫자든 뭐든 입력받기
a = input()

# 받은게 숫자인지 확인해보기
if(type(int(a)) is int):
    b=int(a)
    if b>0:
        if b%2==0:
            print("C")
        else:
            print("D")    
    else:
        if b%2==0:
            print("A")
        else:
            print("B")
else:
    print("숫자를 입력하라니까요?")

