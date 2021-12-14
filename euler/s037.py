import usefulFunctions

tPrimes = [3737]

i = 8
while len(tPrimes) < 11:
    primenessA = usefulFunctions.isPrime(i)
    if primenessA:
        iLst = split(str(i))
        totalPrimeness = True
        while len(iLst) != 1:
            if not isPrime(iLst[:-1]):
                totalPrimeness = False
                
                break
            else:
                iLst.pop()
        if totalPrimeness:
            tPrimes.append(i)
            print(tPrimes)