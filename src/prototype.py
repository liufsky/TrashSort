import RPi.GPIO as GPIO
import time
import picamera

GPIO.setmode(GPIO.BOARD)

class motor:
  """ class to control DC motor with L293D """
  def _init_(self, pin0, pin1):
    self.pin0= pin0
    self.pin1= pin1
    GPIO.setup(pin0, OUTPUT)
    GPIO.setup(pin1, OUTPUT
    # in progress
print("Starting TrashSort . . .")



