def solution(bin1, bin2):
    answer = bin(int(bin1,2)+int(bin2,2))
    return str(answer).replace('0b','')

print(bin(int("100",2)))