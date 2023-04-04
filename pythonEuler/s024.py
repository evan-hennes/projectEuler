import usefulFunctions

nums = [0, 4, 6]

def lexPerm(numList):
  perms = []
  numPerms = usefulFunctions.factorial(len(numList))
  for i in range(len(numList)):
    perm = [num for num in range(i, len(numList))]
    perms.append(perm)
  return perms

print(usefulFunctions.factorial(9) * 2 + usefulFunctions.factorial(8) * 6 + usefulFunctions.factorial(7) * 6 + usefulFunctions.factorial(6) * 2 + usefulFunctions.factorial(5) * 5 + usefulFunctions.factorial(4) + usefulFunctions.factorial(3) * 2 + usefulFunctions.factorial(2) * 2)
#2783915460