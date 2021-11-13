#Create "imput" func 

sysvar = 1

def getStr(text):
  try:
    if text == "":
      getText = input(">")
      return getText
    else:
      getText = input(text)
      return getText
  except:
    print("$")

