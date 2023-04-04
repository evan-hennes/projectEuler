names = open("euler/s022input.txt", "r")
names = names.read()
names = names.split(",")
names = sorted(names)
alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
alphabet = alphabet.split()
charSum = 0
for index, name in enumerate(names):
  name = name[1:len(name) - 1]
  score = 0
  for char in name:
    score += alphabet.index(char) + 1
  charSum += score * (index + 1)
print(charSum)