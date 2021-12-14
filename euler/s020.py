import usefulFunctions

fac = usefulFunctions.factorial(100)
facList = [int(digit) for digit in str(fac)]
print(sum(facList))