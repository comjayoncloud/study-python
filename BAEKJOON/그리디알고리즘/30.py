n = list(input())
# 오름차순 했지만 아직도 str형태.
n.sort(reverse=True)

sum = 0

for i in n:
    # str 형태이기에 int로 형변환 시켜줘야함. sum은 3의 배수인지 확인하기 위한 변수
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    # str 형태를 더해주기
    print(''.join(n))
"""
1. 배열로 한글자씩 받기
2. 30 배수가 되는 조건 검사 후 맞으면 반환
2-1 0이 포함되어야함
2-2 합의 나누기 3이 0이어야됌.
"""

