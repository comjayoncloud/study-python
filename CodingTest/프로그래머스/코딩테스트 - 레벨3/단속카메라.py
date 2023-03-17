def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    print(routes[1])
    # print(routes)
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	)

"""

걸린시간 : 50분
초기 생각한 해결방안 :
    모든 차량 단속용 카메라 한 번은 만나도록 설치
    최소 몇대 카메라 설치해야함?
    [i][0]에는 i 번쨰 차량이 고속도로 진입한지점
    [i][1]에는 나간 지점

    들어온시점<나가는지점 에 설
    -20 , -14 , -18 , -5 # min , 들어온시점 -> -5 , -14 , -18 , -20
    -15 , -5  , -13 , -3 # max , 나간시점   -> -3 , -5 , -13 , -15
    


틀린점 및 해결방안 :
    


다른사람코드 및 리뷰 :



"""