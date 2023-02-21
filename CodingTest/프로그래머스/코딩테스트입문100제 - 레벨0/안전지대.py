def solution(board):
    answer = 0
    bomb=[]
    #1. 1이 있는곳 인덱스를 찾자! 25번 돌려야됨 .for 2번

    for i in range(len(board)):
        for j in range(len(board)):
            # 1과 같으면 인덱스를 bomb 리스트에 추가..
            if board[i][j] ==1:
                bomb.append([i,j])
    print(bomb) # 3 2
    #2. bomb 주변 상,하,좌,우 다 2로 바꾸자 . 범위 체크해야됨..
    for i in range(len(bomb)):
        x = bomb[i][0] 
        y = bomb[i][1]
        
        # 윗줄 존재할때 , 
        #상 3개 바꿀때 2개 바꿀때 1개 바꿀때 안바꿀때 4가지경우
         
        board[x-1][y] = 2
        print(bomb[i][0])
        #하
        board[x+1][y] = 2
        #좌
        board[x][y-1] =2
        #우
        board[x][y+1]=2

    print(board)
    
    return answer

solution([  [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 1, 0, 0],   
            [0, 0, 0, 0, 0]]) 

"""
해결방법
1. 1이 있는곳 index를 찾는다
2. 인덱스를찾으면 그 인덱스 주변으로 0을 2로 바꾼다
3. 다 바꾼후 각 배열들의 0의 갯수를 합해서 리턴한다.
"""


"""
다른사람코드1
    import numpy as np
    def solution(board):
        board = np.array(board)
        for a, b in zip(*np.where(board == 1)):
            board[a-1 if a else 0:a+2, b-1 if b else 0:b+2] = 1
        return len(board[board == 0])

다름사람코드2 
    import numpy as np
    from collections import Counter

    def solution(board):
        n = len(board)
        # pad() 함수를 사용해 주어진 2차원 배열의 상하좌우 1줄씩 -1을 추가한 board_padded 생성
        board_padded = np.pad(board, ((1, 1), (1, 1)), constant_values = -1)
        danger_array = np.pad(board, ((1, 1), (1, 1)), constant_values = -1)
        for i in range(1, n+1):
            for j in range(1, n+1):
                if board_padded[i][j] == 1:
                    for x in range(i-1, i+2):
                        for y in range(j-1, j+2):
                            danger_array[x][y] = 1
        danger_list = danger_array.reshape(1, -1).squeeze()
        answer = Counter(danger_list)[0]
        # 결과 값 반환
        return answer

다른사람코드3
    def solution(board):
        n = len(board)
        danger = set()
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if not x:
                    continue
                danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
        return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)       

다른사람코드4
    def solution(board):
        N = len(board)
        dx = [-1, 1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, -1, 1, -1, 1, -1, 1]

        #지뢰가 설치된 곳
        booms = []
        for x in range(N):
            for y in range(N):
                if board[x][y] == 1:
                    booms.append((x, y))

        #지뢰가 설치된 곳 주변에 폭탄 설치
        for x, y in booms:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    board[nx][ny] = 1

        #폭탄이 설치되지 않은 곳만 카운팅
        count = 0
        for x in range(N):
            for y in range(N):
                if board[x][y] == 0:
                    count += 1

        return count
"""

"""
느낀점 : 너무 어렵고 복잡하다.. for문으로 처리하려다보니 항상 배열의 길이 체크때문에 머리가 아파온다ㅠㅠ
"""