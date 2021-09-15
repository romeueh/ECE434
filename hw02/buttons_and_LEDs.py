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
button_3 = "P9_23"
button_4 = "P9_24"
GPIO.setup(button_1, GPIO.IN)
GPIO.setup(button_2, GPIO.IN)
GPIO.setup(button_3, GPIO.IN)
GPIO.setup(button_4, GPIO.IN)

def update(channel):
  state = GPIO.input(channel)
  if (channel == button_1):
    GPIO.output(LED_1, state);
  if (channel == button_2):
    GPIO.output(LED_2, state);
  if (channel == button_3):
    GPIO.output(LED_3, state);
  if (channel == button_4):
    GPIO.output(LED_4, state);

GPIO.add_event_detect(button_1, GPIO.BOTH, callback=update)
GPIO.add_event_detect(button_2, GPIO.BOTH, callback=update)
GPIO.add_event_detect(button_3, GPIO.BOTH, callback=update)
GPIO.add_event_detect(button_4, GPIO.BOTH, callback=update)

try:
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
