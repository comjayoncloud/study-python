def solution(mylist):
    def f(x):
        return x%2==0
    def g(x):
        return x**2 
    answer = list(map(g,filter(f,mylist)))
    print(answer)
    return answer

solution([3, 2, 6, 7])


"""
의도한바
mylist = [3, 2, 6, 7]
answer = [number**2 for number in mylist if number % 2 == 0]
"""