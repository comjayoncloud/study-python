def solution(common):
    one, two, three = common[:3]
    print(one,two,three)
    if two - one == three - two:
        result = common[-1] + (two-one)
    elif two // one == three // two:
        result = common[-1] * (two//one)  
    return result

solution([1, 2, 3, 4])