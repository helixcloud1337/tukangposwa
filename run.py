#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This tool was build for educational purpose only
Do with your own risk

@TukangPos v1.0
@https://github.com/helixcloud1337/tukangposwa

"""

import webbrowser
import time
import pyautogui as gui
from urllib.parse import quote
from colorama import init
from termcolor import colored
import pyfiglet

init()
ascii_banner = pyfiglet.figlet_format('TukangPos')
print (ascii_banner)
print (colored('Automated tool for sending whatsapp v1.0', 'green'))
time.sleep(6)
interval = 2
position = (934, 445)
txt = open('numbers.txt', 'r')
numbers = txt.readlines()


message = '''

Tukang pos is here

'''

for i in numbers:
    url = 'https://wa.me/{}?text={}'.format(i, message)
    webbrowser.open(url)
    time.sleep(5)
    gui.click(position)
    time.sleep(5)
    gui.press('enter')
    print ('Nomor', i ,'Sukses')
    time.sleep(interval)
