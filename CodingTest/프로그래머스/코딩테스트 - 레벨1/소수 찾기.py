# def solution(n):
#     answer = 0
#     for i in range(2,n+1):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)
#             answer +=1        
#     return answer



# solution(10) 
#2, 3, 5, 7 

# def solution(n):
#     answer = 0 
#     ch = [0]*(n+1)
#     for i in range(2,n+1):
#         if ch[i]==0:
#             answer+=1
#             for j in range(i,n+1,i):
#                 ch[j]=1    
#     return answer


def solution(n):
    num=set(range(2,n+1))
    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
            print(num)
    return len(num)

solution(10) 
