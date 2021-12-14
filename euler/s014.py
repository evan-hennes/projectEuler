
def collatz(n):
  numLoops = 1
  while n != 1:
    if n % 2 == 0:
      n = n / 2
    else:
      n = (3 * n) + 1
    numLoops += 1
  return numLoops
#end function collatz

longest = (0, 0)
for i in range(1000000, 1, -1):
  coll = collatz(i)
  if coll > longest[0]:
    longest = (coll, i)
    print(longest)
print(longest)