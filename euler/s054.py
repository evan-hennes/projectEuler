poker = open("euler/s054input.txt", "r")
poker = poker.read()
valueOrder = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def valSort(val):
  ndx = valueOrder.index(val)
  return ndx
#end function valSort

def getHandValues(hand):
  values = []
  for i in range(len(hand)):
    values.append(hand[i][0])
  #end for loop
  return values
#end function getHandValues

def checkFlush(hand):
  values = getHandValues(hand)
  values = sorted(values, key = valSort)
  if hand[0][1] == hand[1][1] and hand[0][1] == hand[2][1] and hand[0][1] == hand[3][1] and hand[0][1] == hand[4][1]:
    return (True, values[4])
  else:
    return (False,)
  #end selection logic
#end function checkFlush

def checkStraight(hand):
  values = getHandValues(hand)
  values = sorted(values, key = valSort)
  ndx1 = valueOrder.index(values[0])
  if (values[0] == valueOrder[ndx1] and values[1] == valueOrder[ndx1 + 1] and values[2] == valueOrder[ndx1 + 2] and values[3] == valueOrder[ndx1 + 3] and values[4] == valueOrder[ndx1 + 4]):
    return (True, values[4])
  elif (hand[0] == "2" and hand [1] == "3" and hand[2] == "4" and hand[3] == "5" and hand[4] == "A"):
    return (True, values[3])
  else:
    return (False,)
  #end selection logic
#end function straight

def royalFlush(hand):
  if checkFlush(hand)[0]:
    values = getHandValues(hand)
    values = sorted(values, key = valSort)
    if "T" in values and "J" in values and "Q" in values and "K" in values and "A" in values:
      return (True, values[4])
    else:
      return (False,)
    #end inner selection logic
  #end outer selection logic
  else:
    return (False,)
#end function royalFlush

def straightFlush(hand):
  if checkFlush(hand)[0]:
    values = getHandValues(hand)
    values = sorted(values, key = valSort)
    #ndx1 = valueOrder.index(values[0])
    if checkStraight(hand)[0]:
      return (True, values[4])
    else:
      return (False,)
    #end inner selection logic
  #end outer selection logic
  else:
    return (False,)
#end function straightFlush


def fourOfAKind(hand):
  values = getHandValues(hand)
  values = sorted(values, key = valSort)
  for i in values:
    duplicates = values.count(i)
    if duplicates == 4:
      return(True, i)
    else:
      return (False,)
    #end selection logic
  #end for loop
#end function fourOfAKind

def onePair(hand):
  values = getHandValues(hand)
  values = sorted(values, key = valSort)
  for i in values:
    duplicates = values.count(i)
    if duplicates == 2:
      return (True, i)
    else:
      continue
    #end selection logic
  #end for loop
  return (False,)
#end function onePair

def threeOfAKind(hand):
  values = getHandValues(hand)
  values = sorted(values, key = valSort)
  for i in values:
    duplicates = values.count(i)
    if duplicates == 3:
      return (True, i)
    else:
      continue
    #end selection logic
  #end for loop
  return (False,)
#end function threeOfAKind

def fullHouse(hand):
  values = getHandValues(hand)
  values = sorted(values, key = valSort)
  if threeOfAKind(hand)[0]:
    if onePair(hand)[0]:
      return (True, threeOfAKind(hand)[1])
  return (False,)
  #end selection logic
#end function fullHouse

def twoPairs(hand):
  p1 = onePair(hand)
  if not p1[0]: return (False,)
  duplicatesRemoved = [c for c in hand if c[0] != p1[1]]
  p2 = onePair(duplicatesRemoved)
  if not p2[0]: return (False,)
  bestValue = valueOrder[max(valueOrder.index(p1[1]), valueOrder.index(p2[1]))]
  return (True, bestValue)
#end function twoPairs

def highCard(hand):
  values = getHandValues(hand)
  values = sorted(values, key = valSort)
  return values[4]
#end function highCard

def playPoker(hand):
  if royalFlush(hand)[0]:
    return (10, royalFlush(hand)[1])
  elif straightFlush(hand)[0]:
    return (9, straightFlush(hand)[1])
  elif fourOfAKind(hand)[0]:
    return (8, fourOfAKind(hand)[1])
  elif fullHouse(hand)[0]:
    return (7, fullHouse(hand)[1])
  elif checkFlush(hand)[0]:
    return (6, checkFlush(hand)[1])
  elif checkStraight(hand)[0]:
    return (5, checkStraight(hand)[1])
  elif threeOfAKind(hand)[0]:
    return (4, threeOfAKind(hand)[1])
  elif twoPairs(hand)[0]:
    return (3, twoPairs(hand)[1])
  elif onePair(hand)[0]:
    return (2, onePair(hand)[1])
  else:
    return (1, highCard(hand))
#end function playPoker

handList = poker.split("\n")
player1Wins = 0
for i in range(len(handList)):
  hand = handList[i]
  hand1 = hand[:14]
  hand2 = hand[15:]
  hand1 = hand1.split()
  hand2 = hand2.split()
  for j in range(len(hand1)):
    hand1[j] = tuple(hand1[j])
    hand2[j] = tuple(hand2[j])
  if playPoker(hand1)[0] > playPoker(hand2)[0]:
    player1Wins += 1
  elif playPoker(hand1)[0] == playPoker(hand2)[0]:
    if valueOrder.index(playPoker(hand1)[1]) > valueOrder.index(playPoker(hand2)[1]):
      player1Wins += 1
    elif valueOrder.index(playPoker(hand1)[1]) == valueOrder.index(playPoker(hand2)[1]):
      vals1 = sorted(getHandValues(hand1), key = valSort)
      vals2 = sorted(getHandValues(hand2), key = valSort)
      if valueOrder.index(vals1[4]) > valueOrder.index(vals2[4]):
        player1Wins += 1
#finally end for loop  

print(player1Wins)