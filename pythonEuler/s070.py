import usefulFunctions

phiList = usefulFunctions.phiSieve(10000001)
minimum = 12290
for index, phi in enumerate(phiList):
  indexList = usefulFunctions.makeDigitList(index)
  phiAsList = usefulFunctions.makeDigitList(phi)
  if len(indexList) == len(phiAsList) and index != 0 and index != 1:
    indexList = sorted(indexList)
    phiAsList = sorted(phiAsList)  
    if indexList == phiAsList:
      if index / phi < minimum:
        minimum = index / phi
        print(index)

#you got scammed and had to do it in vs smh my head