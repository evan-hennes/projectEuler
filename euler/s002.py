heckFrick = []
x = 1
y = 2
hek = 0
heckFrick = [x, y]

while hek < 4000000:
  hek = x + y
  x = y
  y = hek
  heckFrick.append(hek)

#print(heckFrick)
heckFrick = [i for i in heckFrick if i % 2 == 0]
#print(heckFrick)
print(sum(heckFrick))
