#!/bin/bash

echo i2c2: P9_19, P9_20
config-pin P9_19 i2c 
config-pin P9_20 i2c

echo i2c1: P9_24, P9_26
config-pin P9_24 i2c 
config-pin P9_26 i2c

echo gpio: P9_30, P9_41 #setup for python file
config-pin P9_30 gpio 
config-pin P9_41 gpio

temp1=`i2cget -y 2 0x48` #retrieve temp from sensor 1
tempnum1=$((16#"${temp1:2:4}"))

temp1f=$((($tempnum1 * 9 / 5 ) + 32)) #converting to Fahrenheit
echo "${temp1f}"

temp2=`i2cget -y 2 0x4a` #retrieve temp from sensor 2
tempnum2=$((16#"${temp2:2:4}"))

temp2f=$((($tempnum2 * 9 / 5 ) + 32)) #converting to Fahrenheit
echo "${temp2f}"
