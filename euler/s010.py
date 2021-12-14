def sieveOfEratosthenes(num):
  #make boolean list of all numbers up to num 
  boolList = [True for i in range(num)]
  boolList[0], boolList[1] = False, False
  p = 2
  #start @ smallest prime
  while p ** 2 < num + 1:
    if not boolList[p]:
      p += 1
      continue
    #i starts @ p^2, goes to num, inc by p
    for i in range(p**2, num, p):
      boolList[i] = False #marks nums as not prime
    p += 1
  #creates tuple list of index (int), primeness (bool) and adds to list if primeness is True
  numList = [index for index, primeness in enumerate(boolList) if primeness]
  return numList

print(sieveOfEratosthenes(2000000))