def solution(array, height):
    answer = 0
    for i in array:
        if i >height:
            answer +=1
        else:
            continue
    return answer

solution([149, 180, 192, 170],167)


"""
다른사람코드
    def solution(array, height):
        array.append(height)
        array.sort(reverse=True)
        return array.index(height)
"""