n = int(input())
n = 1000 -n
count = 0
while True:
    if(n<=0):
        break
    elif(n//500>0):
        count+= n//500
        n = n%500
    elif(n//100>0):
        count +=n//100
        n = n%100
    elif(n//50>0):
        count+= n//50
        n = n%50
    elif(n//10>0):
        count += n//10
        n =n%10
    elif(n//5>0):
        count +=n//5
        n =n%5
    elif(n//1>0):
        count +=n//1
        n = n%1

print(count)
        

"""
다른 사람 코드 :
    for문사용
    나처럼 지저분하게 if문으로 길게 하지않고 배열을 써서 깔끔하게 해결함.

a = 1000 - int(input())
b = [500, 100, 50, 10, 5, 1]
count = 0
for i in b:
    count += a // i
    a %= i
print(count)

"""

"""
다른사람 코드 : 
    while문 사용
n = 1000 - int(input())

currency = [500, 100, 50, 10, 5, 1] # 동전의 가치 저장할 리스트 선언
count = 0 # 동전의 개수를 저장할 변수
i = 0 # 동전의 가치 리스트의 인덱스 변수

while n != 0:
  count += n//currency[i] # 동전의 개수를 저장
  n %= currency[i] # 동전의 가치로 나눈 나머지를 저장
  i += 1 # 인덱스를 증가시킨다.

print(count)
"""
