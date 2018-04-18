a =input()

count = 0
size = len(a)
if (size ==0):
  print('0')
else:
  for i in range (size):
    if (a[i] == ' '):
      if (i != size-1 and i != 0):
        count = count+ 1

  if (count ==0):
    if (size !=1):
      print ('1')
    else:
      print ('0')
  else:
    count = count +1
    print (count)
