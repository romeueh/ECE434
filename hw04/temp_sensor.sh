#!/bin/bash

echo i2c1: P9_24, P9_26
config-pin P9_24 i2c 
config-pin P9_26 i2c

echo Reading from TMP101 Sensor (0x49)
cd /sys/class/i2c-adapter/i2c-2/2-0049/hwmon/hwmon0
cat temp1_input 
