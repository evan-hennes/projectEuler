import math

yearArray = [i for i in range(1901, 2001)]
monthArray = [i for i in range(1, 13)]

numFirstSundays = 0
for year in yearArray:
  for month in monthArray:
    m = month
    Y = int(str(year)[2:])
    C = int(str(year)[:2])
    if month == 12:
      if year % 4 == 0 and year != 1900 and year != 2000:
        for i in range(1, 30):
          k = i
          f = (k + (math.floor((2.6*m)-0.2))-(2*C)+Y+(math.floor(Y/4))+(math.floor(C/4))) % 7
          if f == 0 and i == 1:
            print(month, i, year)
            numFirstSundays += 1
      else:
        for i in range(1, 29):
          k = i
          f = (k + (math.floor((2.6*m)-0.2))-(2*C)+Y+(math.floor(Y/4))+(math.floor(C/4))) % 7
          if f == 0 and i == 1:
            print(month, i, year)
            numFirstSundays += 1
    elif month == 1 or month == 3 or month == 5 or month == 6 or month == 8 or month == 10:
      for i in range(1, 32):
        k = i
        f = (k + (math.floor((2.6*m)-0.2))-(2*C)+Y+(math.floor(Y/4))+(math.floor(C/4))) % 7
        if f == 0 and i == 1:
          print(month, i, year)
          numFirstSundays += 1
    else:
      for i in range(1, 31):
        k = i
        f = (k + (math.floor((2.6*m)-0.2))-(2*C)+Y+(math.floor(Y/4))+(math.floor(C/4))) % 7
        if f == 0 and i == 1:
          print(month, i, year)
          numFirstSundays += 1

print(numFirstSundays)