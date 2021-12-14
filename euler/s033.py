yes = []
#n = 16
#d = 64
for n in range(10, 100):
  for d in range(n + 1, 100):
    frac = n / d
    #print(frac)
    nList = [int(d) for d in str(n)]
    dList = [int(d) for d in str(d)]
    if 0 in nList or 0 in dList:
      continue
    if nList[0] == dList[0]:
      #print("no")
      reduced = nList[1] / dList[1]
    elif nList[1] == dList[0]:
      #print("balls")
      reduced = nList[0] / dList[1]
    elif nList[1] == dList[1]:
      #print("to")
      reduced = nList[0] / dList[0]
    elif nList[0] == dList[1]:
      #print("cum")
      reduced = nList[1] / dList[0]
    else:
      #print("penis")
      continue
    if reduced == frac:
      print(reduced)
      print("no balls to cum")
      yes.append(frac)

product = 1
for f in yes:
  product *= f

print(product)
print((product).as_integer_ratio())