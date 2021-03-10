## yishdi
### How to use:
##### Make sure the `ys_config.txt` is in the `📁 installer` folder. Using a custom `config` file? go [here](https://github.com/K-Dub1234/yishdi/blob/Master/CUSTOM.md).
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

#### (.html) ys_:
```html
// Makes a button linking to this GitHub page
<!DOCTYPE html>
<html>
<head>
<script>
function openWin() {
  window.open("https://github.com/K-Dub1234/yishdi");
}
</script>
</head>
<body>

<form>
  <input type="button" value="See it on GitHub" onclick="openWin()">
</form>

</body>
</html>
```
#### (.js) ys_mptps-handler:
```javascript
// Mandatory Ping Transfer Protocol Secure (MPTPS)
pingID = Math.floor(Math.random() * 1.001);
var pings = {from:101, to:101, ID:pingID}; // use this to declare ports.
// 101 is the standard port number.
var trnsdata = pings.from * pings.to;
window.alert('mptps://ping.js.ys');
```
