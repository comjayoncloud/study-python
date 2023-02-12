def solution(mylist):
    return sum(mylist,[])

solution([[1], [2]])


"""
의도한바 

방법 1 - sum함수

방법 2 - itertools.chain
    import itertools
    list(itertools.chain.from_iterable(my_list))

방법 3 - itertools와 unpacking
    import itertools
    list(itertools.chain(*my_list))

방법 4 - list comprehension 이용
    [element for array in my_list for element in array]

방법 5 - reduce 함수 이용 1
    from functools import reduce
    list(reduce(lambda x, y: x+y, my_list))

방법 6 - reduce 함수 이용 2
    from functools import reduce
    import operator
    list(reduce(operator.add, my_list))

방법 7 - numpy 라이브러리의 flatten 이용 (원소의 길이가 동일한 경우에만 사용)
    import numpy as np
    np.array(my_list).flatten().tolist()
"""