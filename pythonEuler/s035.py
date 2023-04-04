import usefulFunctions

primes = usefulFunctions.sieveOfEratosthenes(1000000)
#print(len(primes))

circ = set()
for p in primes:
  rots = usefulFunctions.rotations(p)
  #print(rots)
  yes = []
  if p in circ:
    continue
  for r in rots:
    if r in primes:
      yes.append(True)
    else:
      yes.append(False)
  if False not in yes:
    for r in rots:
      circ.add(r)
      #print(r)
    print(len(circ))
print(len(circ))
