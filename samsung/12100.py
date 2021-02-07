import collections

# 보드의 크기
N = int(input())

# 보드 정보
board = [list(map(int, input().split())) for _ in range (N)]
queue = collections.deque()
answer = 0


def get(i,j):
    if board[i][j] != 0:
        queue.append(board[i][j])
        board[i][j] = 0


def merge(i, j, di, dj): # row index, column index, y방향, x방향
    while queue:
        x = queue.popleft() # 움직이려는 블록 값을 가져온다. FIFO
        if board[i][j] ==0: # 0이라면 그대로 놓는다.
            board[i][j] = x
        elif board[i][j] == x: # 값이 일치한다면
            board[i][j] = x*2 # 합쳐지므로 2배로 증가
            i, j = i+di, j+dj
        else: # 값이 일치하지 않으면
            i, j = i+di, j+dj
            board[i][j] = x


def merge(i, j, di, dj): # row_index, column_index, y방향 x방향
    while queue:
        x = queue.popleft() #블록 값을 가져옴
        if board[i][j] == 0: #0이면
            board[i][j] = x
        elif board[i][j] == x: #값이 일치하면
            board[i][j] = x * 2
            i, j = i+di, j+dj
        else: #값이 일치하지 않으면
            i, j = i +di, j + dj
            board[i][j] = x

# 상화좌우 움직이기 함수
def movement(k):
    if k == 0: # 위로 이동, 블락들이 위로 모두 이동시켜야 함
        for j in range(N):
            for i in range(N):
                get(i,j)
            merge(0, j, 1, 0)
    elif k == 1: #아래로 이동
        for j in range(N):
            for i in range(N-1, -1, -1):
                get(i,j)
            merge(N-1, j, -1, 0)
    elif k == 2: #왼쪽으로 이동
        for i in range(N):
            for j in range(N):
                get(i,j)
            merge(i, 0, 0, 1)
    else: #오른으로 이동
        for i in range(N):
            for j in range(N-1, -1, -1):
                get(i,j)
            merge(i, N-1, 0, -1)

def solve(count):
    global board, answer

    if count == 5:
        for i in range(N):
            answer = max(answer, max(board[i]))
        return

    b = [x[:] for x in board] # 원래 보드를 복사
    for k in range(4):
        movement(k)
        solve(count+1)
        board = [x[:] for x in b]



solve(0)
print (answer)

