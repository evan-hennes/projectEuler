import usefulFunctions

triangle = open("euler/s067input.txt", "r")
triangle = triangle.read()

triangle = triangle.split("\n")
for i in range(len(triangle)):
  triangle[i] = triangle[i].split()
  triangle[i] = [int(num) for num in triangle[i]]

print(usefulFunctions.maxTriangleSum(triangle))
