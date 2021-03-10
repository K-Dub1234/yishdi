## yishdi
### How to use:
##### Make sure the `ys_config.txt` is in the `📁 installer` folder. Using a custom `config` file? go [here](LINK).
##### Running `installer.py` will set up and deploy yishdi.
### Usage:
#### ys_errors:
```python
err(errcode):
  print("There was an error: " + errcode)
# EX: err('404 page not found')
```
#### ys_configure:
```python
blankfile():
  f = open("ys_cofig.txt", "w")
  f.write(rbinry())
  f.close()
  
makefile(data):
  f = open("ys_config.txt", "a")
  f.write(bin(data))
  f.close()
  # EX: makefile(1234) (must be a number. no decimals)
  # rbinry() is a custom random binary number generator
```
#### ys_bindings:
```python
bind():
  print('_-_-_-_-_-_-_-_-binding files-_-_-_-_-_-_-_-_')
  time.sleep(1)
  ping = r.randint(1111, 9999)
  f = open("ys_ping.data.txt", "w")
  if ping == '__null af__':
    ping = r.randint(1111, 9000)
  f.write(bin(ping))
  f.close()
# binds ys_ping.data.txt file
split():
  ping = '__null af__'
  binder = []
# splits ping
  
end():
  binder = ["PROGRAM ENDED"]
  ping = '__null af__'
  print('goodbye')
  exit('goobye')
# ends file

```
