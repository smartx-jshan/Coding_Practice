import collections
from sys import stdin



n, m = map(int, stdin.readline().split())

graph = [list(stdin.readline()) for _ in range(n)]

red = [0, 0]
blue = [0, 0]

# red 저장
# blue 저장

# red와 blue 좌료를 획득 후, 그 자리를 이동할 수 있는 . 으로 변경
for i in range (n):
    for j in range(m):
        if graph[i][j] == 'R':
            graph[i][j] = '.'
            # 레드 저장
            red = [i, j]
        elif graph[i][j] == 'B':
            graph[i][j] = '.'
            # 블루 저장
            blue = [i,j]

print (red)
print (blue)

def movement(x, y, dx, dy):
    move = 0
    while graph[x+dx][y+dy] != '#':

        if graph[x+dx][y+dy] == 'O':
            return 0, 0, 0
        x += dx
        y += dy
        move += 1
    return x, y, move

def bfs():
    visit = {}
    queue = collections.deque([red + blue])
    print (queue)


    visit[red[0], red[1], blue[0], blue[1]] = 0
    while queue:
        rx, ry, bx, by = queue.popleft()
        for dx, dy in (-1,0), (1,0), (0,-1), (0, 1):
            nrx, nry, rmove = movement(rx, ry, dx, dy)
            nbx, nby, bmove = movement(bx, by, dx, dy)
            print (dx, dy, "인 경우 ", "nred:", nrx, nry, rmove, "Nblue:", nbx,nby,bmove)

            # 파란공이 탈출한 경우
            if nbx == 0 and nby == 0:
                continue

            # 파란공은 탈출 안하고 빨간공이 탈출한경우
            elif nrx == 0 and nry == 0:
                print (visit[rx,ry,bx,by] + 1)
                return
            # 두 공이 같은 방향으로 이동된 경우, 이동을 많이 한놈 이전으로 돌려놔야 함
            elif nrx == nbx and nry == nby:
                if rmove > bmove:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
            # 방문한 곳이 아닌 경우
            if (nrx, nry, nbx, nby) not in visit:
                visit[nrx, nry, nbx, nby] = visit[rx, ry, bx, by] +1
                queue.append([nrx, nry, nbx, nby])

        if not queue or visit[rx, ry, bx, by] >= 10:
            print (-1)
            return

bfs()




