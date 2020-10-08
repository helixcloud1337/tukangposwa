#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This tool was build for educational purpose only
Do with your own risk

@TukangPos v1.1
@https://github.com/helixcloud1337/tukangposwa

"""

import webbrowser
import time
import pyautogui as gui
from urllib.parse import quote
from colorama import init
from termcolor import colored
import pyfiglet
import clipboard

init()
ascii_banner = pyfiglet.figlet_format('TukangPos')
print (ascii_banner)
print (colored('Automated tool for sending whatsapp v1.0', 'green'))
time.sleep(6)
interval = 2
position = 934,445 #position for clicking ok
close = 292,20 #coordinate to close page
txt = open("no.txt", "r") #phone number list
numbers = txt.readlines()


message = open("message.txt", "r").read() #change your message
clipboard.copy(message)

for i in numbers:
 url = 'https://wa.me/{}'.format(i)
 #url = 'https://web.whatsapp.com/send?phone={}&text&app_absent=0'.format(i)
 webbrowser.open(url)
 time.sleep(3)
 gui.click(position)
 time.sleep(3)
 gui.hotkey('ctrl', 'v')
 gui.press('enter')
 gui.click(close)
 time.sleep(interval)
