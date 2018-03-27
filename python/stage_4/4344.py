a = int(input())

for i in range (a):
  b = list(map(int,input().split()))
  size = int(b[0])
  sum = 0
  for j in range (size):
    sum = sum + b[j+1]
  mean = sum/size
  count = 0
  for k in range (size):
    if (b[k+1] > mean):
      count = count +1
  temp = count / size * 100
  print ("%0.3f%%" % temp)
