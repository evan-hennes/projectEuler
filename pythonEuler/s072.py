def phiSieve(num):
  # make list of all numbers up to num 
  phiList = [i for i in range(num + 1)]
  p = 2
  # start @ smallest prime
  while p <= num:
    if phiList[p] == p: # number is prime
      # i starts @ p * 2, goes to num, inc by p
      for i in range(p * 2, num + 1, p):
        phiList[i] *= 1 - (1 / p) # multiplies to remove multiples of p from num
      phiList[p] -= 1 # phi of prime number is itself minus 1
    p += 1
  phiList = [round(phi) for phi in phiList]
  return phiList
#end function phiSeive

print(sum(phiSieve(1000000)) - 1) # 303963552391