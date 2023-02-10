def solution(box, n):
    answer = ( box[0]//n ) * ( box[1]//n) *(box[2]//n)
    return answer


"""
다른사람코드
import math

def solution(box, n):
    return math.prod(map(lambda v: v//n, box))
"""