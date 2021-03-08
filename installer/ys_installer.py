# YISHDI SYSTEM 1.1.2

import os
import ys_errors as err
import ys_configure as conf
import ys_bindings as bind
tick = 1

# runs

print('/SYSTEM ARMED...')
print('/VERSION READY...')
print('/-----------------V 1.1.2 YISHDI SYSTEM READY-----------------')

# checks if the file exists, or if it needs to create one.

if not os.path.exists("ys_config.txt"):
  conf.blankfile()
  
print('/READING "ys_config.txt" FILE...')
if os.path.exists("ys_config.txt"):
  
  # reads file for needed data (9 digits) (1, 23, 456, 7890 etc.)
  
  f= open("ys_config.txt", "r")
  while tick != 0:
    print(f.read(tick))
    tick += 1
  tick = 0
print('/ cofig file read')
print('/done.')
print('/-----------------READY FOR SOMETHING-----------------')
