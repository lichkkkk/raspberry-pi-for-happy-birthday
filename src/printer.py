
# -*- coding: utf-8 -*-
from __future__ import print_function

from PIL import Image
from adafruit_lib.Adafruit_Thermal import Adafruit_Thermal

class Printer:

    _SEPARATE_LINE = '\n' + ''.join(['_'] * 32) + '\n'

    def __init__(self):
        self._printer = Adafruit_Thermal(
                '/dev/serial0',
                19200,
                timeout=3.0)
        self._printer.setCharset(15)

    _FEED_NUM = 3

    def writeSingleLine(self):
        self._printer.write(self._SEPARATE_LINE)
        self._printer.feed(self._FEED_NUM)

    def printText(self, msg, end=True):
        self._printer.write(msg.encode('utf-8'))
        if end:
          self.writeSingleLine()

    def printImage(self, img_path, end=True):
        self._printer.printImage(Image.open(img_path).resize((256, 256)), True)
        if end:
          self.writeSingleLine()

#Test
#printer = Printer()

# printer.printText(u' 我想你'.encode('utf-8'))
# printer.printText('111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
# printer.printText('I miss you\n')
# printer.printImage('../data/img/moe.jpeg')
