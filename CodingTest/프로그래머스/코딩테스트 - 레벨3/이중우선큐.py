def solution(operations):
    answer = []
    final = [0,0]
    for i in range(len(operations)):
        if operations[i]=="D 1":
            operations[i]="A"
        elif operations[i]=="D -1":
            operations[i]="B"
    for i in range(len(operations)):
        if operations[i][0]=="I":
            answer.append(int(operations[i][2:]))
        elif operations[i][0]=="A":
            if not answer:
                continue
            else:
                answer.remove(max(answer))
            # print(answer)
        elif operations[i][0]=="B":
            if not answer:
                continue
            else :
                answer.remove(min(answer))
    
    if not answer:
        return final
    else :
        final[0]= max(answer)
        final[1]=min(answer)

        
    return final

# solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
# 16 -5643 -> 16 -> [] -> [] -> 123 -> [] 

solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])
# -45 653 -> -45 -> -45 -642 45 97 -> -45 45 -642 -> -45 45 -> -45 45 333
"""

걸린시간 : 19분

생각한 해결방안 :
    I - 주어진 숫자
    D 1 - 최댓값삭제
    D -1 - 최솟값삭제
    
    1. 각 배열 원소의 첫 글자로 뭘 할지 정하기에 .. D -1 , D 1을 편하게 치환하자.
틀린점 :
    없음
다른사람코드 및 리뷰 :
    힙q를 이용한 풀이
    import heapq
    def solution(a):
        heap = []
        max_heap = []

        for i in a:
            current = i.split()
            if current[0]=='I':
                num = int(current[1])
                heapq.heappush(heap,num)
                heapq.heappush(max_heap,(num*-1,num))
            else:
                if len(heap)==0:
                    pass
                elif current[1]=='1':
                    max_value= heapq.heappop(max_heap)[1]
                    heap.remove(max_value)
                elif current[1]=='-1':
                    min_value = heapq.heappop(heap)
                    max_heap.remove((min_value*-1,min_value))
        if heap:
            return [heapq.heappop(max_heap)[1],heapq.heappop(heap)]
        else:
            return[0,0]
            
    힙은 무엇인가 차곡차곡 쌓아올린 더미.
    우선순위 큐는 가장 우선순위가 높은 데이터를 의미한다.
    힙의 종류는 최대힙 , 최소 힙이 있다.
    힙을 저장하는 표준적인 자료구조는 배열
    구현을 쉽게하기 위해 배열의 첫번째 인덱스 0 은 사용되지 않는다.


"""