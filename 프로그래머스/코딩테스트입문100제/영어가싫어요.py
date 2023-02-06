def solution(numbers):
    a = numbers
    a = a.replace('zero','0')
    a = a.replace('one','1')
    a = a.replace('two','2')
    a = a.replace('three','3')
    a = a.replace('four','4')
    a = a.replace('five','5')
    a = a.replace('six','6')
    a = a.replace('seven','7')
    a = a.replace('eight','8')
    a = a.replace('nine','9')
    a = int(a)
    return a

solution("onetwothreefourfivesixseveneightnine"	)

"""
다른사람 풀이
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)
"""
"""
느낀점:
    enumerate 함수를 처음 알게되었다. 활용잘하자!
"""