color = input("Choose a color of either Red, Green, or Blue: ")

def newPrint(color, word):
  if color == "red" or color == "Red":
    print("\033[31m", word, sep="", end="")
  elif color=="green" or color == "Green":
    print("\033[32m", word, sep="", end="")
  elif color=="blue" or color == "Blue":
    print("\033[34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print()
print("Super Subroutine")
print()
print("With my ", end="")
newPrint(color, "new program")
newPrint("default", " I can just call it ('and') ")
newPrint(color, "it will print in that color ")