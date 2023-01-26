n,k = map(int,input().split())
d = []
for i in range (n):
    a = int(input())
    d.append(a)

count = 0
d.sort(reverse=True)

# for 10번 실행후 나가는 while 문
while True:
    #10번 진행 d 배열 0부터 끝까지.
    for i in range(n):
        count += k//d[i]
        k = k%d[i]
    print(count)
    break


"""
풀이과정
1. 입력값 파악해서 n,k 및 10번 실행할 input,저장할 배열 선언
2. 입력 받는 즉시 빈 배열에 요소 추가 (순서대로 이기에 append 사용)
3. 나눈 몫을 저장할 count 선언 
4. 큰 수부터 나누어 하므로 배열을 오름차순으로 바꿈 (sort(reverse=True)사용)
5. 설탕 배달문제에서 얻은 힌트 이용. (10번 돌리고 (for문) break 하는 while문 작성)

"""