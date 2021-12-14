import usefulFunctions

s = 0
for i in range(1000000):
  iList = usefulFunctions.makeDigitList(i)
  iSum = sum([(x ** 5) for x in iList])
  if iSum == i and i != 1:
    s += i
    print(s)

