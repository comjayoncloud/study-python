def solution(dot):
    x = dot[0]
    y = dot[1]
    if x >0 :
        if y >0:
            return 1
        else:
            return 4
    else:
        if y>0:
            return 2
        else:
            return 3
    return 0

solution([2,4])


"""
다른사람코드1
    def solution(dot):
        quad = [(3,2),(4,1)]
        return quad[dot[0] > 0][dot[1] > 0]

다른사람코드2
    def solution(dot):
        a, b = 1, 0
        if dot[0]*dot[1] > 0:
            b = 1
        if dot[1] < 0:
            a = 2
        return 2*a-b

"""