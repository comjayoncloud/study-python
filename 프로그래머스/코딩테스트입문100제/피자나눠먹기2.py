def solution(n):
    pizza = 1
    while (pizza*6)%n!=0:
        pizza +=1
        print(pizza)
    return pizza

"""
"""