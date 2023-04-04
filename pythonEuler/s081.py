matrix = open("euler/s081input.txt", "r")
matrix = matrix.read()
matrix = matrix.split("\n")

for i in range(len(matrix)):
  matrix[i] = [int(s) for s in matrix[i].split(",")]

mingus = [
  [131, 673, 224, 103, 18],
  [201, 96, 342, 965, 150],
  [630, 803, 746, 422, 111],
  [537, 699, 497, 121, 956],
  [805, 732, 524, 37, 331]
]

def maxMatrixSum(m):
  print(m)
  for i in reversed(range(len(m) - 1)):
    m[len(m) - 1][i] += m[len(m) - 1][i + 1]
    m[i][len(m) - 1] += m[i + 1][len(m) - 1]
  print(m)
  for i in reversed(range(len(m) - 1)):
    for j in reversed(range(len(m) - 1)):
      x1 = m[i][j]
      x2 = m[i][j + 1]
      y = m[i + 1][j]
      print(x1, x2, y)
      if x1 + x2 < x1 + y:
        s = x1 + x2
      else:
        s = x1 + y
      m[i][j] = s
  return m[0][0]
# end function maxMatrixSum

print(maxMatrixSum(mingus))