# 1   3,5,7,9    13,17,21,25    31, 37, 43, 48

s = 1
c = 1
for i in range(2, 1001, 2):
  for j in range(4):
    c += i
    s += c

print(s)