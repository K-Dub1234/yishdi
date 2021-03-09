{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 AppleColorEmoji;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 ## yishdi\
### How to use:\
##### Make sure the `ys_config.txt` is in the `
\f1 \uc0\u55357 \u56513 
\f0  installer` folder. Using a custom `config` file? go [here](LINK).\
##### Running `installer.py` will set up and deploy yishdi.\
### Usage:\
#### ys_errors:\
```python\
err(errcode):\
  print("There was an error: " + errcode)\
# EX: err('404 page not found')\
```\
#### ys_configure:\
```python\
blankfile():\
  f = open("ys_cofig.txt", "w")\
  f.write(rbinry())\
  f.close()\
  \
makefile(data):\
  f = open("ys_config.txt", "a")\
  f.write(bin(data))\
  f.close()\
  # EX: makefile(1234) (must be a number. no decimals)\
  # rbinry() is a custom random binary number generator\
```\
#### ys_bindings:\
```python\
bind():\
  print('_-_-_-_-_-_-_-_-binding files-_-_-_-_-_-_-_-_')\
  time.sleep(1)\
  ping = r.randint(1111, 9999)\
  f = open("ys_ping.data.txt", "w")\
  if ping == '__null af__':\
    ping = r.randint(1111, 9000)\
  f.write(bin(ping))\
  f.close()\
# binds ys_ping.data.txt file\
split():\
  ping = '__null af__'\
  binder = []\
# splits ping\
  \
  end():\
  binder = ["PROGRAM ENDED"]\
  ping = '__null af__'\
  print('goodbye')\
  exit('goobye')\
# ends file\
\
```}