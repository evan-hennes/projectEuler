import usefulFunctions

words = usefulFunctions.convertToVar("euler/s042input.txt", ",")
alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
alphabet = alphabet.split()
print(alphabet)

def t(n):
  triNum = (n / 2) * (n + 1)
  return triNum
# end function t

triNums = []
for i in range(1, 355):
  triNums.append(t(i))
#print(triNums)

numTriWords = 0
for word in words:
  end = len(word) - 1
  word = word[1:end]
  charSum = 0
  for char in word:
    charSum += alphabet.index(char) + 1
  if charSum in triNums:
    numTriWords += 1
    print(word, charSum)
print(numTriWords)