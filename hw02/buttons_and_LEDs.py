#!/usr/bin/env python3
#chmod +x buttons_and_LEDs.py
#Author: Eliza Romeu

import Adafruit_BBIO.GPIO as GPIO 
import time 

LED_1 = "P9_12"
LED_2 ="P9_11"
LED_3 ="P9_21"
LED_4 ="P9_22"
GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(LED_3, GPIO.OUT)
GPIO.setup(LED_4, GPIO.OUT)

button_1 = "P9_17"
button_2 = "P9_18"
button_3 = "P9_21"
button_4 = "P9_22"
GPIO.setup(button_1, GPIO.IN)
GPIO.setup(button_2, GPIO.IN)
GPIO.setup(button_3, GPIO.IN)
GPIO.setup(button_4, GPIO.IN)

def led_off(channel):
  if (channel == button_1):
    GPIO.output(LED1, GPIO.LOW);
  if (channel == button_2):
    GPIO.output(LED2, GPIO.LOW);
  if (channel == button_3):
    GPIO.output(LED3, GPIO.LOW);
  if (channel == button_4):
    GPIO.output(LED4, GPIO.LOW);

def led_on(channel):
  if (channel == button_1):
    GPIO.output(LED1, GPIO.HIGH);
  if (channel == button_2):
    GPIO.output(LED2, GPIO.HIGH);
  if (channel == button_3):
    GPIO.output(LED3, GPIO.HIGH);
  if (channel == button_4):
    GPIO.output(LED4, GPIO.HIGH);

GPIO.add_event_detect(button_1, GPIO.FALLING, callback=led_off)
GPIO.add_event_detect(button_2, GPIO.FALLING, callback=led_off)
GPIO.add_event_detect(button_3, GPIO.FALLING, callback=led_off)
GPIO.add_event_detect(button_4, GPIO.FALLING, callback=led_off)

GPIO.add_event_detect(button_1, GPIO.RISING, callback=led_on)
GPIO.add_event_detect(button_2, GPIO.RISING, callback=led_on)
GPIO.add_event_detect(button_3, GPIO.RISING, callback=led_on)
GPIO.add_event_detect(button_4, GPIO.RISING, callback=led_on)

try:
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
