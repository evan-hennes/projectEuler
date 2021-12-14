
prodSum = 0
nums = [str(i) for i in range(1, 10)]
prods = []
for j in range(1, 100):
  for i in range(j + 1, 10000):
    product = i * j
    hek = list(str(i) + str(j) + str(product))
    hek.sort()
    if hek == nums:
      prods.append((i, j, product))
      prodSum += product
print(prodSum)
print(sum(set(a[2] for a in prods)))