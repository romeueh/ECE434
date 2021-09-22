i2cset -y 2 0x48 0x03 0x16
i2cset -y 2 0x49 0x03 0x16

temp1=`i2cget -y 2 0x48` #retrieve temp from sensor 1

temp1f=$((( $temp1 * 9 ) / 5 + 32 )) #converting to Fahrenheit
echo $temp1f

temp2=`i2cget -y 2 0x49` #retrieve temp from sensor 2

temp2f=$((( $temp2 * 9 ) / 5 + 32 )) #converting to Fahrenheit
echo $temp2f
