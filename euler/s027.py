import math
import usefulFunctions

def quadratic(a, b, n):
  return (n ** 2) + (a * n) + b

def isPrime(num):
  #print(num)
  if num < 3: return False
  if math.sqrt(abs(num)).is_integer(): return False
  if num % 2 == 0: return False
  for i in range(3, int(math.sqrt(abs(num))), 2):
    if num % i == 0:
      return False
  return True
# end function isPrime

prime = True
largestNumPrimes = 0
for a in range(-999, 1000):
  for b in range(-1000, 1001):
    n = 0
    while isPrime(quadratic(a, b, n)):
      n += 1 #not pog
    if n > largestNumPrimes:
      largestNumPrimes = n
      print(a * b)
      # green check ez
      # look at this u there?  
      # ok gamer needs to sleep now
      # good night good night gamer one line code man
      # ok one line code man. yes. based. absolutely
