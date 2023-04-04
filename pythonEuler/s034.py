import usefulFunctions

totalSum = 0
for i in range(1, 1000000):
  iList = usefulFunctions.makeDigitList(i)
  facSum = 0
  for digit in iList:
    facSum += usefulFunctions.factorial(digit)
  if facSum == i and i != 1 and i != 2:
    totalSum += i
    print(totalSum)
print(totalSum)