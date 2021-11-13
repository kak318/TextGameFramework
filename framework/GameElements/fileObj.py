#objects

def newObj(name, where):
  opn = "config/", name
  obj = open(opn, "w+")
  obj.write(name, where)