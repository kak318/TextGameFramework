#sample game

from framework.GameElements.fileInput import getStr

print("PLAY? [y/n]")
yn = getStr("y/n? ")
if yn == "y":
  print("y")
elif yn == "n":
  print("n")
else:
  print("?")