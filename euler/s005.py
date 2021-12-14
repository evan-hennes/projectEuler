def divisibleByAll(upper):
  num = upper
  divisibility = False
  while divisibility == False:
    for i in range(1, upper + 1):
      if num % i != 0:
        num += upper
        break
      if i == upper:
        divisibility = True
  return num

print(divisibleByAll(20))
