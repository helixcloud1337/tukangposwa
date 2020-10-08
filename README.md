# TukangPos WA
Automated tool for sending whatsapp v1.1 using webbrowser

# Install
###### Requirements
```
Python 3.7.x is required
```
###### Install requirements
```
pip -r requirements.txt
```

# How to use
###### Edit your phone number list (no.txt)
use your country code without + (e.g: 62) separated with break lines
```
62123456789
62123456789
62123456789
62123456789
```

###### Edit your message (message.txt)
Works with
```
This is message
```
```
This
is
message
```


Bold Text using asterisk:
```
*This is message*
```

Italic Text using underscore:
```
_This is message_
```

Striketrough Text using tilde:
```
~This is message~
```

# Navigate the close
###### Use pyautogui for navigate the close position
```
import pyautogui
while True:
  print(pyautogui.position())
```
