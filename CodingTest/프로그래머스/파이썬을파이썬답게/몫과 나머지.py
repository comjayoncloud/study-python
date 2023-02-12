a, b = map(int, input().strip().split(' '))
c = divmod(a,b)
print(*c)


# divmod : 몫과 나머지를 튜플형식으로 반환하는 함수