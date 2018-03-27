a = int(input())
b = list(map(int,input().split()))
num = max(b)
sum = 0
for i in range (a):
  temp = int(b[i])
  value = temp * 100 / num
  sum = sum + value

mean = sum / a

print ("%0.2f" % mean)
