
# 시험장의 개수
N = int(input())
# 시험장의 응시자 수
people = list(map(int, input().split()))

B, C = map(int, input().split())

#print (N)
#print (people)
#print (B)
#print (C)

count = 0

for i in people:
    if B >= i: #총 감독관이 시험장 응시자 수 보다 큰 경우
        count += 1 # 한명 카운트하고 넘어감
    else: # 총 감독관이 시험장 응시자 수 보다 작은 경우
        left = i - B #(양수이다, 남은사람)
        count += 1
        num, res = divmod(left, C)
        if res == 0:
            count = count + num
        else:

            count = count + num + 1

    #print (count)

print (count)

