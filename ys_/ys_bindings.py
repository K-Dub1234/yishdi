# ys_bindings
ping = '__null af__'
binder = []
import time
import random as r

def bind():
  print('_-_-_-_-_-_-_-_-binding files-_-_-_-_-_-_-_-_')
  time.sleep(1)
  ping = r.randint(1111, 9999)
  f = open("ys_ping.data.txt", "w")
  if ping == '__null af__':
    ping = r.randint(1111, 9000)
  f.write(bin(ping))
  f.close()
  
def split():
  ping = '__null af__'
  binder = []

def end():
  binder = ["PROGRAM ENDED"]
  ping = '__null af__'
  print('goodbye')
  exit('goobbye')

end()
