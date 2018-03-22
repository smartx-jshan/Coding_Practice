a = int(input())
for i in range (a):
  for k in range (i):
    print (" ", end='')
  for j in range (a, i, -1):
    print ("*", end='')
  print ("")

