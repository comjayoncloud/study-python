def solution(dots):
    
    x =[]
    y =[]
    for i in dots:
        
        x.append(i[0])
        y.append(i[1])
    a = max(x)-min(x)
    b = max(y)-min(y)    
            
    return a*b

solution([[1, 1], [2, 1], [2, 2], [1, 2]]	)

# 넓이 ? x * y



"""
다른사람코드
    def solution(dots):
        return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
"""