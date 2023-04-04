import math

def d(num):
  divisors = []
  if math.sqrt(num).is_integer():
    divisors.append(int(math.sqrt(num)))
  for i in range(1, num):
    if num % i == 0:
      divisors.append(i)
  return sum(divisors)
#end function d

amicableSum = 0
for i in range(10001):
  if d(d(i)) == i and d(i) != i:
    amicableSum += i
    print(i, d(i), amicableSum)