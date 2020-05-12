
from __future__ import print_function

import time
import threading
from time import localtime, strftime

from http_client import HTTPClient
from screen_display import ScreenDisplay
from printer import Printer
from button import Button
from led import LED
from speaker import Speaker

pre_msg = ''
screen = ScreenDisplay()
#http = HTTPClient()
printer = Printer()
button = Button()


def play_song():
  speaker = Speaker()
  speaker.start()
  speaker.play(Speaker.HappyBirthday, 200)
  speaker.close()

#printer.printText('I\'m working now!\n\n', False)

while button.read() == 0:
  pass

th = threading.Thread(target=play_song)
th.start()

screen.show()

printer.printText(strftime(' %a, %d %b %Y %H:%M:%S %Z\n', localtime()), False)
#printer.printText('I\'m working now!\n\n', False)

printer.printText('Moe Happy Birthday !!!\n\n', False)
printer.printImage('../data/img/moe.jpeg', True)

th.join()

led = LED()
led.start()
led.blink(5)
led.close()

"""
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
"""
