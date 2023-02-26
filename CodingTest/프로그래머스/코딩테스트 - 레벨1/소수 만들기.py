import itertools
import math

def solution(nums):
    answer = 0
    combo = list(itertools.combinations(nums,3))
    # print(sum(combo[0]))

    for i in combo:
        i = sum(i)
        # 만든 조합이 소수인지 판별 , if문을 만나면 소수가 아니기에 for문에서 나오고 for문에서 무사히 통과하면 소수이기에
        # for 문 밖에서 answer+=1
        for j in range(2,int(math.sqrt(i)+1)):
            if i%j == 0:
                break
        else:
            answer+=1
    return answer

solution([1,2,3,4])
# solution([1,2,7,6,4])

# 3개를 더했을때 소수가 되는경우. combination ,3 조합
