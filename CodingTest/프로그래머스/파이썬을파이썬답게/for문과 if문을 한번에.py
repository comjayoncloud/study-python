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
의도한바 : #1이 아닌 #2를 쓰자
    #1
    mylist = [3, 2, 6, 7]
    answer = []
    for number in mylist:
        if number % 2 == 0:
            answer.append(number**2) # 들여쓰기를 두 번 함

    #2
    mylist = [3, 2, 6, 7]
    answer = [number**2 for number in mylist if number % 2 == 0]

"""