
pence = [1, 2, 5, 10, 50, 100]

final = 200
combinations = set()
counter = 0

for i in range(0, 201, 100):
  for j in range(i, 201, 50):
    for ballsack in range(j, 201, 20):
      for k in range(ballsack, 201, 10):
        for m in range(k, 201, 5):
          for n in range(m, 201, 2):
            counter += 1
            print(counter + 1)


