def sieveOfEratosthenes(num):
  #make list of all numbers up to num 
  numList = [i for i in range(2,num)]
  numNdx = 0
  p = 2
  #start @ smallest prime
  while p ** 2 < num + 1:
    for i in range(p**2, num, p):
      #print(i)
      if i % p == 0 and i in numList:
        #print(i)
        numList.remove(i)
    numNdx += 1
    p = numList[numNdx]
    print(p)
  print(numList[10000])

sieveOfEratosthenes(110000)