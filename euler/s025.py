import usefulFunctions

num = 1
numLoops = 1
while len(str(num)) < 1000:
  numLoops += 1
  num = usefulFunctions.fibonacci(numLoops)
  #print(numLoops)
print(numLoops)