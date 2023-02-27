def solution(number, limit, power):
    count=0
    number_arr=[]
    number_arr_power=[]
    # 1. 1~number만큼 배열생성
    for i in range(1,number+1):
        number_arr.append(i)
    
    # 2. 각 number의 약수 개수를 구해서 number_power에 넣음
    for n in number_arr:
        for i in range(1,int(n**(1/2))+1):
            if n%i==0:
                count+=1
                if ((i**2)!=n):
                    count+=1
                
        number_arr_power.append(count)
        count =0
    
    #3. number_power에서 limit을 넘기면 그 원소의 power는 받음 power가 됨
    for i in range(len(number_arr_power)):
        if number_arr_power[i]>limit:
            number_arr_power[i] = power


    return sum(number_arr_power)



solution(5,3,2)

"""
해결방안
1. 1~number만큼 받음
2. 각 수만큼 약수의 개수를 구함(power)
3. limit을 넘으면 넘으면 그 공격력은 power 가됨

"""

# def solution(number, limit, power):
#     count=0
#     number_arr=[]
#     number_arr_power=[]
#     # 1. 1~number만큼 배열생성
#     for i in range(1,number+1):
#         number_arr.append(i)
    
#     # 2. 각 number의 약수 개수를 구해서 number_power에 넣음
#     for n in number_arr:
#         for i in range(1,n+1):
#             if n%i==0:
#                 count+=1
#         number_arr_power.append(count)
#         count =0
    
#     #3. number_power에서 limit을 넘기면 그 원소의 power는 받음 power가 됨
#     for i in range(len(number_arr_power)):
#         if number_arr_power[i]>limit:
#             number_arr_power[i] = power


#     return sum(number_arr_power)
# => 시간초과