import random as r
def blankfile():
  f = open("ys_cofig.txt", "w")
  f.write(rbinry())
  f.close()
  
def makefile(data):
  f = open("ys_config.txt", "a")
  f.write(bin(data))
  f.close()
  
def rbinry():
    return bin(r.randint(1, 99999999999))
