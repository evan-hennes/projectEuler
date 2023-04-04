import math

factor = 0
number = 600851475143

""""
def checkPrime(number):
  if number > 1:
    for i in range(2, math.ceil(math.sqrt(number))):
      if number % i == 0:
        return False
  return True    
"""

def sieveOfEratosthenes(num): 
  numList = [i for i in range(2,num)]
  p = 2
  while p ** 2 < num + 1:
    for i in range(p**2, num, p):
      #print(i)
      if i % p == 0 and i in numList:
        #print(p)
        numList.remove(i)
    p += 1
  print(numList)

sieveOfEratosthenes(number)