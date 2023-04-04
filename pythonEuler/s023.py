import usefulFunctions

abundantNums = set() # list would be fine here but see below
for i in range(1, 28123):
  if i % 1000 == 0:
    print(i)
  isAbundant = False
  if sum(usefulFunctions.checkDivisors(i)) > i: # fix ur check divisors its bonked i think
    abundantNums.add(i)
print(abundantNums)

# i recomend using a set to record the numbers that can be made or a bool list 
abundantSums = set()
for num in abundantNums:
  for num1 in abundantNums:
    abSum = num + num1
    if abSum > 28123:
      break
    else:
      abundantSums.add(abSum)
    
      
# then here you can loop to 28123 again and add stuff 
nonAbundantSum = 0
for i in range(1, 28124):
  if i not in abundantSums:
    nonAbundantSum += i

print(nonAbundantSum)