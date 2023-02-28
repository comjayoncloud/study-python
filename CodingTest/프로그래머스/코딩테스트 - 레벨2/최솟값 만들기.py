def solution(A,B):
    answer = 0
    A = sorted(A,reverse=True)
    B = sorted(B,reverse=False)
    for _ in range(len(A)):
        answer +=A[-1]*B[-1]
        # 쓴 원소들은 pop 으로 제거
        A.pop()
        B.pop()
        
    return answer

solution([1, 4, 2],[5, 4, 4])


"""
#1 
    min(A) * max(B)

걸린시간 : 8분

생각한 해결방안 :
    문제를 이해하니 min(A) * max(B) 를 통해 최솟값을 구함. 쓴 원소들은 pop으로 없애면 될듯.
    min,max를 사용하지않고 sorted를 통해 A는 내림차순 B는 오름차순으로해서 마지막 원소 [-1]를 이용했고
    pop()을 쓰면 마지막 원소부터 나가니 따로 index 및 min,max를 사용하지않고 해결하였음

틀린점 :
    없음
다른사람코드 및 리뷰 :

    def getMinSum(A, B):
        return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])

    => for 문에 2개의 변수를 사용하기 위해 zip을 사용 , A,B는 sorted 이용. 
    => sorted를 이용했기에 각각 리스트 곱 해야할곳들을 매치시켰음 .그후 반환한 list를 sum으로 해결 
    => 한줄로 깔끔하게 끝난게 매력적
"""