lst1 =  [75]
lst2 =  [95, 64]
lst3 =  [17, 47, 82]
lst4 =  [18, 35, 87, 10]
lst5 =  [20, 4, 82, 47, 65]
lst6 =  [19, 1, 23, 75, 3, 34]
lst7 =  [88, 2, 77, 73, 7, 63, 67]
lst8 =  [99, 65, 4, 28, 6, 16, 70, 92]
lst9 =  [41, 41, 26, 56, 83, 40, 80, 70, 33]
lst10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
lst11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
lst12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
lst13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
lst14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
lst15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

longLst = [lst1, lst2, lst3, lst4, lst5, lst6, lst7, lst8, lst9, lst10, lst11, lst12, lst13, lst14, lst15]

def maxTriangleSum(triangle):
  for i in reversed(range(len(triangle))):
    for j in range(len(triangle[i]) - 1):
      x1 = triangle[i][j]
      x2 = triangle[i][j + 1]
      y = triangle[i - 1][j]
      print(x1, x2, y)
      sum = 0
      if y + x1 > y + x2:
        sum = y + x1
      else:
        sum = y + x2
      triangle[i - 1][j] = sum
  return triangle[0][0]
#end function maxTriangleSum
      

print(maxTriangleSum(longLst))