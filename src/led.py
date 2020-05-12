
import time
from RPi import GPIO

class LED:

  GPIO_PORT_1 = 5
  GPIO_PORT_2 = 6
  GPIO_PORT_3 = 12
  GPIO_PORT_4 = 13

  
  def start(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.GPIO_PORT_1, GPIO.OUT)
    GPIO.setup(self.GPIO_PORT_2, GPIO.OUT)
    GPIO.setup(self.GPIO_PORT_3, GPIO.OUT)
    GPIO.setup(self.GPIO_PORT_4, GPIO.OUT)

  def close(self):
    self.off()
    GPIO.cleanup()

  def blink(self, Hz):
    
    p1 = GPIO.PWM(self.GPIO_PORT_1, Hz)
    p2 = GPIO.PWM(self.GPIO_PORT_2, Hz)
    p3 = GPIO.PWM(self.GPIO_PORT_3, Hz)
    p4 = GPIO.PWM(self.GPIO_PORT_4, Hz)
    
    delay = .25/Hz
    p1.start(50)
    time.sleep(delay)
    p2.start(50)
    time.sleep(delay)
    p3.start(50)
    time.sleep(delay)
    p4.start(50)
    time.sleep(3)
    p1.stop()
    p2.stop()
    p3.stop()
    p4.stop()

  def on(self):
    GPIO.output(self.GPIO_PORT_1, True)
    GPIO.output(self.GPIO_PORT_2, True)
    GPIO.output(self.GPIO_PORT_3, True)
    GPIO.output(self.GPIO_PORT_4, True)

  def off(self):
    GPIO.output(self.GPIO_PORT_1, False)
    GPIO.output(self.GPIO_PORT_2, False)
    GPIO.output(self.GPIO_PORT_3, False)
    GPIO.output(self.GPIO_PORT_4, False)


"""
Test
"""
#led = LED()
#led.start()
#led.blink(4)
#led.off()
#led.close()
