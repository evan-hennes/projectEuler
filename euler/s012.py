import math

def checkNumDivisors(num):
  numDivisors = 0
  if math.sqrt(num).is_integer():
    numDivisors += 1
  for i in range(1, int(math.sqrt(num))):
    if num % i == 0:
      numDivisors += 2
  return numDivisors

triNum = 0
j = 1
while True:
  triNum += j
  #print(triNum)
  divisors = checkNumDivisors(triNum)
  #print(divisors)
  if divisors >= 500:
    break
  j += 1

print(triNum)

