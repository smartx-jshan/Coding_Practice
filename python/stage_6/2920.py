a = input().split()

def asc (a):
  count = 1
  num = len(a)

  for i in range (num):
    if ( int(a[i]) == count):
      count = count + 1
      if (i != num -1):
        continue
      else:
        if (count == 9):
          return True
        else:
          return False

def des (a):
  count = 8
  num = len(a)

  for i in range (num):
    if ( int(a[i]) == count):
      count = count - 1
      if (i != num -1):
        continue
      else:
        if (count == 0):
          return True
        else:
          return False


if ( asc (a)):
  print ("ascending")
elif ( des(a)):
  print ("descending")
else:
  print ("mixed")


