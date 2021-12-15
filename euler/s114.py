from functools import cache

fullRow = 50

@cache
def fill(row):
    minLen = 3
    if row < minLen:
        return 1
    nice = 0
    for i in range(minLen, row + 1):
        pog = row - i - 1
        nice += fill(pog)
    nice += fill(row - 1)
    return nice


print(fill(fullRow))