
from __future__ import print_function

import time
from time import localtime, strftime

from http_client import HTTPClient
from screen_display import ScreenDisplay
from printer import Printer
from button import Button
from led import LED

pre_msg = ''
#screen = ScreenDisplay()
http = HTTPClient()
printer = Printer()
button = Button()
led = LED()

printer.printText('I\'m working now!\n\n', False)

while button.read() == 0:
  pass

printer.printText(strftime('%a, %d %b %Y %H:%M:%S %Z\n', localtime()), False)
printer.printText('I\'m working now!\n\n', False)
printer.printImage('../data/img/lichkkkk.jpeg', True)


while True:
    while button.read() == 0:
      pass
    led.on()
    msg = http.get()
    if msg['text'] != None:
      printer.printText(msg['text'], False)
    if msg['img'] != None:
      printer.printImage(msg['img'], True)
    
    time.sleep(1)
    led.off()

