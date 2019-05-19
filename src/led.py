
import time
from RPi import GPIO

class LED:

  GPIO_PORT = 12
  
  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.GPIO_PORT, GPIO.OUT)

  def __del__(self):
    self.off()
    GPIO.cleanup()

  def on(self):
    GPIO.output(self.GPIO_PORT, True)

  def off(self):
    GPIO.output(self.GPIO_PORT, False)


"""
Test
"""
"""
led = LED()
led.on()
time.sleep(2)
led.off() 
"""
