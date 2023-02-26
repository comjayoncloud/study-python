
def solution(n, lost, reserve): 
    answer = 0 
    #중복제거
    reserve_del = set(reserve)-set(lost) # 1,5
    
    #중복제거
    lost_del = set(lost)-set(reserve) 
    print(reserve_del)
    for i in reserve_del: 
        if i-1 in lost_del: 
            lost_del.remove(i-1) 
            
        elif i+1 in lost_del: 
            lost_del.remove(i+1) 
            
    answer = n - len(lost_del)
    
    return answer


solution(5,[2,4],[1,2,5])

"""
전체학생수 n -> 1,2,3,4,5
도난 당한 학생들 배열 lost -> 2,4
여벌의 체육복 가져온 학생들 reverse -> 1,3,5

\ 여벌 체육복을 가져온 학생이 도난 당했을수도 있다. 이경우엔 줄수가없다 lost 2 == reverse 2면 빌려줄수가없다.



3,4,5,8,9,12,24
"""