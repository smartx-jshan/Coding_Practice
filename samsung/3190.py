import collections

N = int(input())
K = int(input())
#사과 정보
apple = [list(map(int, input().split())) for _ in range (K)]
L = int(input())
#뱀 움직임 정보
movement = [list(map(str, input().split())) for _ in range(L)]

'''
N = 10
K = 5
apple = [[1, 5], [1, 3], [1, 2], [1,6], [1,7]]
L = 4
movement = [['8', 'D'], ['10','D'], ['11', 'D'],['13','L']]
'''

direction = [0,1] #뱀의 초기 방향

# 카운트
count = 0

# 뱀의 크기와 정보 (마지막 행이 머리이다.)
snake = collections.deque([[0,0]])

# apple을 보정하기
for i in range(len(apple)):
    apple[i][0] -= 1
    apple[i][1] -= 1




while True:
    # 초를 먼저 늘리고
    count +=1

    # 뱀을 움직이자
    head = [snake[-1][0] + direction[0], snake[-1][1] + direction[1]]

    #print (snake)

    if head[0] == N or head[1] == N or head[0] < 0 or head[1] <0: #보드를 넘어가면 중단
        break

    if head in snake: #뱀의 머리가 자신의 좌표에 속하면
        break

    # 뱀의 머리에 사과가 있다면
    if head in apple:
        snake.append(head)
        # 사과를 지워야한다
        apple.remove(head)
    else: # 사과가 없다면
        snake.popleft() # 꼬리를 자르고
        snake.append(head) #머리를 생성

    # 방향 전환이 있다면 방향전환
    if movement and int(movement[0][0]) == count:
        # L(왼쪽) D(오른족)

        if direction[0] == 0: #열쪽으로 움직이고 있을때
            if direction[1] > 0: #양수이면 오른쪽으로 움직이고 있을때
                if movement[0][1] == 'L':
                    direction[0] = -1
                    direction[1] = 0
                else:
                    direction[0] = 1
                    direction[1] = 0
            else: #왼쪽으로 움직이고 있으면
                if movement[0][1] =='L':
                    direction[0] = 1
                    direction[1] = 0
                else:
                    direction[0] = -1
                    direction[1] = 0
        else: # 행쪽으로 움직이고 있을때
            if direction[0] > 0: #양수이면 아래쪽으로 움직이고 있을 때
                if movement[0][1] =='L':
                    direction[0] = 0
                    direction[1] = 1
                else:
                    direction[0] = 0
                    direction[1] = -1
            else:
                if movement[0][1] =='L':
                    direction[0] = 0
                    direction[1] = -1
                else:
                    direction[0] = 0
                    direction[1] = 1
        # 방향 전환이 끝났으면 movement 0번을 없애야 함
        del movement[0]

print (count)



