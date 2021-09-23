#!/usr/bin/env python3
#chmod +x temp_sensor.py

import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

sensor1 = 0x48 
alert1 = "P9_31"
GPIO.setup(alert1, GPIO.IN) 

sensor2 = 0x49 
alert2 = "P9_32"
GPIO.setup(alert2, GPIO.IN)

bus = smbus.SMBus(2)

def update(channel):
  if(channel == alert1):
    print("Threshold reached on temp 1")
    temp = bus.read_byte_data(sensor1,0)
  if(channel == alert2):
    print("Threshold reached on temp 2")
    temp = bus.read_byte_data(sensor2,0)
    
   temp = temp*9/5 +32
   print(temp)
   time.sleep(5)
    
GPIO.add_event_detect(alert1, GPIO.BOTH, callback=update)
GPIO.add_event_detect(alert2, GPIO.BOTH, callback=update)

try:
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
