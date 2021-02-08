
K = int(input()) # 테스트 케이스 개수


for testcase in range(1, K+1):
    N, O, M = map(int, input().split())
    number = list(map(int, input().split()))
    operation = list(map(int, input().split()))
    target = int(input())
    '''
    N = 5
    O = 3
    M = 10 # 터치 제한
    number = [8, 7, 1, 2, 6]
    operation = [2, 4, 3]
    target = 981
    '''

    length = dict() #해당 숫자의 터치 개수를 저장
    check_list = [ False for _ in range(1000)] # 해당 숫자가 체크되었는지 확인 0에서 999까지만 가능함

    # 초기화 진행
    for num in number:
        length[num] = 1 #터치 초기화
        check_list[num] = True # 체크리스트 체크

    # 10의 자리 두개 만드는 거 진행
    for i in range(1, 10): # 1에서 9까지
        if i in length:
            #print (i)
            for j in range(0, 10): # 0에서 9 까지
                if j in length:
                    if check_list[i*10+j] == False: #한번도 안 찾아졌다면
                        length[i*10 + j] = 2
                        check_list[i*10+j] = True

    for i in range(10, 100): #세 자리수 만들기다
        if i in length:
            for j in range(0,10):
                if j in length:
                    if check_list[i*10+j] == False: #한번도 안찾아졌다면
                        length[i*10+j] = 3
                        check_list[i*10+j] = True

    # 여기까지 하면 그냥 수, 터치로 만들수 있는 수를 저장한 것임

    answer = -1

    if target in length: # 여기까지 만들었는데 있으면 출력
        answer = length[target] # 터치수를 answer에 저장
    else: #만약에 없다면

        for i in range(3, M): # 3에서 M-1까지
            #i는 터치 횟수이다
            for j in range(999, 0 , -1): #999에서 1까지 왜 거꾸로 할까??
                if j not in length or length[j] + 2 > i: # j가 length에 없거나, length + 2가 i보다 크면 i 터치 횟수+ 1만큼에서는 획득이 안되므로 스킵
                    continue

                for k in range(999,0,-1): #다시 999에서 1까지
                    if not check_list[k] or length[k] + length[j] + 1 > i: #체크리스트에 없거나, 터치 회수 충족이 안되면
                        continue

                    for op in operation:
                        if op == 1:
                            if j+ k < 1000:
                                if j+k not in length:
                                    length[j+k] = length[j] + length[k] + 1
                        elif op ==2:
                            if j-k >=0:
                                if j-k not in length:
                                    length[j-k] = length[j] + length[k] + 1
                        elif op == 3:
                            if j * k < 1000:
                                if  j*k not in length:
                                    length[j*k] = length[j] + length[k] + 1
                        elif op == 4:
                            if j//k not in length:
                                length[j//k] = length[j] + length[k] + 1

                        if target in length:
                            answer = i + 1
                            break
                    if answer != -1:
                        break
            if answer != -1:
                break

    print ("#%d" %testcase, answer)







