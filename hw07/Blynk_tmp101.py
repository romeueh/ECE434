#!/usr/bin/env python3
# Blink read the temperature from a TMP101 and display it
import blynklib
import blynktimer
import os
import smbus

# Use i2c bus 1
bus = smbus.SMBus(2) 

# Use address 0x48
tempAddr = 0x48

# Get the autherization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH')

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
# create timers dispatcher instance
timer = blynktimer.Timer()

# Register Virtual Pins
# The V* says to response to all virtual pins
@blynk.handle_event('write V*')
def my_write_handler(pin, value):
    print('Current V{} value: {}'.format(pin, value))

oldtemp = 0
# Code below: register a timer for different pins with different intervals
# run_once flag allows to run timers once or periodically
@timer.register(vpin_num=10, interval=0.5, run_once=False)
def write_to_virtual_pin(vpin_num=1):
    global oldtemp
    # Open the file with the temperature
        #f = open(BMP085, "r")
    temp=  bus.read_byte_data(tempAddr,0) #f.read()[:-1]     # Remove trailing new line
    # Convert from mC to C
    #temp = int(temp)/1000
    #f.close()
    # Only display if changed
    if(temp != oldtemp):
        print("Pin: V{} = '{}".format(vpin_num, str(temp)))
        # Send to blynk
        blynk.virtual_write(vpin_num, temp)
        oldtemp = temp

while True:
    blynk.run()
    timer.run()
