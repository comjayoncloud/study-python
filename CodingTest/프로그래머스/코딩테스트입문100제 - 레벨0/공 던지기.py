
""" 
답은 맞는데 런타임에러..

def solution(numbers, k):
    if len(numbers)%2 ==0:
        numbers = numbers[0::2]
    else:
        numbers = numbers[0::2] + numbers[1::2]
   
    if k > len(numbers):
        k = k-len(numbers)-1
    else:
        k = k-1
    
    result = numbers[k]
     
    return result

# solution([1, 2, 3, 4],2) 
# solution([1, 2, 3,4,5,6],5)
# solution([1, 2, 3] , 2)
"""

def solution(numbers,k):
    players = numbers[0::2] if len(numbers)%2==0 else numbers[0::2]+numbers[1::2]
    return players[k%len(players)-1]



"""
다른사람코드

def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]
"""

