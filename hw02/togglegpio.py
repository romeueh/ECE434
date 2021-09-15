#!/usr/bin/env python3
#chmod +x togglegpio.py
import Adafruit_BBIO.GPIO as GPIO
import time

LED1 = "P9_12"
GPIO.setup(LED1, GPIO.OUT)

while(1):
    GPIO.output(LED1, GPIO.LOW)
    time.sleep(0.005)
        
    GPIO.output(LED1, GPIO.HIGH)
    time.sleep(0.005)
