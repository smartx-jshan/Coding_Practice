a = input()
count = 0

a = int(a)
fix = a

while True:
  if (a < 10):
    a = a *10 + a
    count = count + 1
    if (a == fix):
      print (count)
      break
  else:
    number1 = a //10
    number2 = a % 10
    number3 =  number1 + number2
    if ( number3 < 10):
      a = number2*10 + number3
      count = count +1
      if (a == fix):
        print (count)
        break
    else:
      a = number2 *10 + (number3 % 10)
      count = count + 1
      if (a == fix):
        print (count)
        break 
