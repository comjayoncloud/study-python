
# A - Sort + pop
def solution(arr):
    
    arr = sorted(arr,reverse=True)
    arr.pop()
    return [-1] if len(arr)==0 else arr

# B - min + index + (remove or pop or del)
def solution(arr):

    ## remove or pop or delete
    # arr.remove((min(arr)))
    # arr.pop(arr.index(min(arr)))
    del arr[arr.index(min(arr))]
    return [-1] if len(arr)==0 else arr

# solution([4,3,2,1])
solution([10])
"""
해결방법
    A. sort로 내림차순해서 배열 pop(마지막원소가 나가기때문)
    B. min과 index 이용해서 해결

분석 및 느낀점
    코드에서 별 길이 차이가 나지않는다 .간단해서 그런거 같기도 하다..
"""