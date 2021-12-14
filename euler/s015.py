gridSize = 20

def numPaths(size):
  numPts = (size + 1) ** 2
  pathList = [1 for i in range(numPts)]
  multiple = size + 1
  startingPt = len(pathList) - 1
  while True:
    if startingPt == size:
      return pathList[0]
    if startingPt % multiple == 0:
      startingPt -= 1
    else:
      previous = startingPt - 1
      previous2 = startingPt - multiple
      leftUpNdx = previous2 - 1
      leftUpVal = sum([pathList[previous], pathList[previous2]])
      pathList[leftUpNdx] = leftUpVal
      startingPt -= 1


print(numPaths(gridSize))