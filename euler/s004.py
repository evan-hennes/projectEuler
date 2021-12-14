def makeDigitList(num):
  digitList = []
  while num > 0:
    digitList.append(num % 10) # gets the last digit
    num //= 10
  digitList.reverse()
  return digitList


def isPalindrome(num):
  digitList = makeDigitList(num)
  for i in range(len(digitList) // 2):
    if digitList[i] != digitList[-i-1]:
      return False
  return True

largestPalindrome = 0
for i in range(100, 999):
  for j in range(i, 999):
    if isPalindrome(i * j) and i * j > largestPalindrome:
      largestPalindrome = i * j
    
print(largestPalindrome)