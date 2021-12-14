import usefulFunctions

def decToBin(num):
  return int(bin(num).replace('0b', ''))

palList = []
for i in range(1000000):
  pal10 = usefulFunctions.isPalindrome(i)
  palBin = usefulFunctions.isPalindrome(decToBin(i))
  if pal10 and palBin:
    palList.append(i)
print(sum(palList))