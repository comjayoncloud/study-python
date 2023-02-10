def solution(price):
    
    if 500000<= price:
        return  int(price - (price/100*20))
    if 300000<=price:
        return  int(price - (price/100*10))
    if 100000<=price:
        return  int(price - (price/100*5))
    
    return price


"""
다른사람 풀이
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
"""