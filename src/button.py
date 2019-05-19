
import time
import threading
from RPi import GPIO

class Button:

  def __init__(self, port=16):
    self._gpio_port = port
    self._counter = self._AtomicCounter()    

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self._gpio_port, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(
        self._gpio_port,
        GPIO.FALLING,
        callback = lambda channel : self._counter.increment())

  def __del__(self):
    GPIO.cleanup()

  def checkStatus(self):
    """
    Return whether the button is pushed down at this moment
    """
    return GPIO.input(self.GPIO_PORT) == 0

  def read(self):
    """
    Return how many times the button has been pushed
    since last read.
    WARNING: the count is not accurate at all!!
    """
    return self._counter.readAndClear()
  

  class _AtomicCounter:
    
    def __init__(self, initial=0):
      self._value = initial
      self._lock = threading.Lock()

    def increment(self, num=1):
      with self._lock:
        self._value += num
        return self._value

    def readAndClear(self):
      with self._lock:
        value = self._value
        self._value = 0
        return value

"""
Test
"""
"""
b = Button()

while True:
  time.sleep(1)
  print b.read()
"""
