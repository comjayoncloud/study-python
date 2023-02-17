
def solution(num, total):
    mid = total //num
    half = num //2
    top = mid + half +1
    bot = top - num
    answer = [i for i in range(bot,top)]
    
    return answer

solution(3,12)


"""
다른사람코드1:
    def solution(num, total):
        return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]


다른사람코드2:
    def solution(num, total):
        if num % 2 == 1:
            return list(range(total//num-num//2, total//num+num//2+1))
        else:
            return list(range(total//num-num//2+1, total//num+num//2+1))
"""