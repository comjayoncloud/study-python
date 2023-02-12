num = int(input().strip())
print(num)
answer ="ABCD...(중간생략)..XYZ"
if num == 0:
    print(answer.lower())
elif num == 1:
    print(answer.upper())