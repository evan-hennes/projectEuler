sumSquare = 0
for i in range(1, 101):
  sumSquare += i ** 2
#print(sumSquare)

squareSum = 0
for i in range(1, 101):
  squareSum += i
squareSum = squareSum ** 2
#print(squareSum)

print(squareSum - sumSquare)