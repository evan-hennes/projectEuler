import usefulFunctions, math
from decimal import *
getcontext().prec = 2000

def longestRepeatedSequence(lst):
  guess = 1
  maxLen = len(lst) / 2
  for i in range(2, int(maxLen)):
    if lst[0:i] == lst[i:2*i]:
      return i
  return guess
# end function longestRepeatedSequence

longest = (0, 0)
for d in range(2, 1001):
  frac = Decimal(1) / Decimal(d)
  frac = int(str(frac)[2:])
  digitList = usefulFunctions.makeDigitList(frac)
  # print(digitList)
  seq = longestRepeatedSequence(digitList)
  if seq > longest[0]:
    longest = (seq, d)
    print(longest)
  