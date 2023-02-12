import itertools
def solution(mylist):
    answer = sorted(list(itertools.permutations(mylist, len(mylist))),reverse=False)
    print(answer)
    return answer

solution([2, 1])
solution([1, 2, 3])


"""
의도한바
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 순열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 순열 만들기
"""