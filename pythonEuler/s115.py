from functools import cache

@cache
def fill(m, n):
    if n < m:
        return 1
    tot = 0
    for i in range(m, n + 1):
        pog = n - i - 1
        tot += fill(m, pog)
    tot += fill(m, n - 1)
    return tot

i = 50
while True:
    result = fill(50, i)
    if result > 1000000:
        break
    else:
        i += 1
print(i)