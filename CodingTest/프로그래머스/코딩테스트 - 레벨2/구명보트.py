def solution(people, limit):

    # 몸무게를 오름차순 정렬
    people.sort()

    # 시작, 끝 인덱스
    start, end = 0, len(people)-1

    # 보트의 수
    count = 0

    while start <= end:

        # 보트의 수 증가
        count += 1

        # 두 명(몸무게가 가장 적은 사람, 몸무게가 가장 많은 사람)을 태우거나
        if (people[start] + people[end] <= limit):
            start += 1
            end -= 1

        # 한 명(몸무게가 가장 많은 사람)을 태웁니다.   
        else:
            end -= 1

    return count
# solution([20,20,20,20,10,80,90],100)
# solution([70, 50, 80, 50],100) #3
solution([70, 80, 50],100) #3

"""

걸린시간 : 40분

생각한 해결방안 :
    구명보트를 최대한 적게 사용하여 모든 사람을 구출하고자한다.
    1. 배열생성 초기화될때마다 카운트될 변수 생성
    2. sorted한 people의 첫번째 원소는 무조건들어가야함으로 not(answer)을 사용하여 넣음
    3. 2번째 원소부터 비교해야됨 . answer의 합과 새로들어올 원소의 합이 limit을 넘기지 말아야한다.
    4. 넘기면 answer 초기화 시키고 count +=1 

틀린점 :
    50 ,50 , 70, 80 에서 3개 배가나온 경우가 50+50 , 70 , 80 이기에 sort하고 첫번째 수는 무조건 새배열에 넣고 그다음부턴
    새배열의 합 + 다음 숫자가 limit을 초과하는지 안하는지 확인했는데 if else가 너무 많이 붙고 복잡해졌고 길을 잃었다.

다른사람코드 및 리뷰 :
    원소를 일일이 제거하는 방식보단 인덱스만 변경하는 것이 속도가 빠르다.
    투 포인터를 이용한 해결방안이다. 그리고 조건도 잘못 이해했다.
    맞는 조건은 가벼운 사람 + 무거운 사람 , 무거운사람 2가지 경우의 조건이였다. 
"""