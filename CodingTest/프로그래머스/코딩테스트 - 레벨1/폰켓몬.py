def solution(nums):
    # 중복을 없애자     
    a = set(nums)

    if len(nums)/2 > len(a):
        return len(a)
    else:
        return len(nums)/2 
    return 0
solution([3,1,2,3])
# solution([3,3,3,2,2,2])

"""
다른사람코드
    def solution(ls):
        return min(len(ls)/2, len(set(ls)))
"""