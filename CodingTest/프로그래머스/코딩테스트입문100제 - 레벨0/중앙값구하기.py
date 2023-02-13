def solution(array):
    array = sorted(array,reverse=True)
    return array[len(array)//2]

solution([1, 2, 7, 10, 11])


"""
다른사람코드1
    def solution(array):
        return sorted(array)[len(array) // 2]
"""