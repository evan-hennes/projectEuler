multiplesOf3 = []
multiplesOf5 = []

multiple = 5
x = 0
while x < 1000:
  if x % 15 == 0:
    x += multiple
    continue
  else:
    multiplesOf5.append(x)
  x += multiple

multiple = 3
x = 0
while x < 1000:
  multiplesOf3.append(x)
  x += multiple

finalSum = sum(multiplesOf3) + sum(multiplesOf5)
print(finalSum)
