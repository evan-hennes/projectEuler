distinctTerms = set()

for a in range(2, 101):
  for b in range(2, 101):
    distinctTerms.add(a ** b)

#print(sorted(distinctTerms))
print(len(distinctTerms))