
from __future__ import print_function

import time
import math
import threading

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

from PIL import ImageFont

from debug_utils import debug_print

# TODO: make this a singleton
class ScreenDisplay:
    """
    Class to talk with the 128 * 64 LED screen.
    How to use this:

        screen = ScreenDisplay()
        screen.show('hello, world')

        screen.off() # turn off screen
        screen.on() # turn on screen
    """

    @debug_print
    def __init__(self):
        self.serial_ = i2c(port=1, address=0x3C)
        self.device_ = ssd1306(self.serial_)

    # TODO: format long text to multi lines
    @debug_print
    def show(self, msg1='Moe', msg2='Happy Birthday!'):
        font1 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 18)
        font2 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 14)
        with canvas(self.device_) as display:
            display.rectangle(self.device_.bounding_box, outline='white', fill='black')
            display.text((55, 10), msg1, font=font1, fill='white')
            display.text((5, 35), msg2, font=font2, fill='white')

    @debug_print
    def on(self):
        self.device_.show()

    @debug_print
    def off(self):
        self.device_.hide()

"""
Test
"""
#dp = ScreenDisplay()
#dp.show()
#time.sleep(3)
