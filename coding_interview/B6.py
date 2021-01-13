from typing import List


def solution(m: int, n: int, board: List[str])->int:
    board = [list(i) for i in board]
    #print (board)

    while True:

        marked = []
        # find pattern
        for i in range(m-1):
            for j in range (n-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '#':
                    marked.append([i,j])

        #print (marked)
        # delete pattern
        for i, j in marked:
            board[i][j] = board[i][j+1] = board[i+1][j] = board[i+1][j+1] = '#'
        #print (board)

        # replace board
	for _ in range(m):
            for i in range(1, m):
                for j in range(n):
                    if board[i][j] == '#':
                    	board[i][j], board[i-1][j] = board[i-1][j], '#'
        #print (board)

        # terminate loop
        if not marked:
            break

    #find the number of deleted blocks
    count = 0
    for i in board:
        count += (i.count('#'))

    return count


m = 4
n = 5
m2 = 6
n2 = 6
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
board2 = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print (solution(m2, n2,board2))
