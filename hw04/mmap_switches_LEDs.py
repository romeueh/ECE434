#!/usr/bin/env python3
# Credit: https://graycat.io/tutorials/beaglebone-io-using-python-mmap/
import time, struct
from mmap import mmap

GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
GPIO_DATAIN = 0x138

GPIO0_startaddr = 0x44e07000
GPIO0_endaddr = 0x44e07fff
GPIO0_size = GPIO0_endaddr-GPIO0_startaddr
button0 = 1<<26
LED0 = 1<<27

GPIO1_startaddr = 0x4804c000
GPIO1_endaddr = 0x4804c000
GPIO1_size = GPIO1_endaddr-GPIO1_startaddr
LED1 = 1<<17 
button1 = 1<<14

with open("/dev/mem", "r+b" ) as h:
  mem0 = mmap(h.fileno(), GPIO0_size, offset=GPIO0_startaddr)
with open("/dev/mem", "r+b" ) as f:
  mem1 = mmap(f.fileno(), GPIO1_size, offset=GPIO1_startaddr)

packed_reg0 = mem0[GPIO_OE:GPIO_OE+4]
packed_reg1 = mem1[GPIO_OE:GPIO_OE+4]

reg0_status = struct.unpack("<L", packed_reg0)[0]
reg1_status = struct.unpack("<L", packed_reg1)[0]

reg0_status &= ~(LED0)
reg1_status &= ~(LED1)

mem0[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg0_status)
mem1[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg1_status)

try:
  while(True):
    button0_packed = mem0[GPIO_DATAIN:GPIO_DATAIN+4] #same process used as above
    button0_status = struct.unpack("<L", button0_packed)[0] 
    if (button0_status0 & button0 ) == button0:
      mem0[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LED0)
    else:
      mem0[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LED0)
      
    button1_packed = mem1[GPIO_DATAIN:GPIO_DATAIN+4] 
    button1_status = struct.unpack("<L", button1_packed)[0]
    if (button1_status & button1 ) == button1:
      mem1[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LED1)
    else: 
      mem1[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LED1)

except KeyboardInterrupt:
  mem0.close()
  mem1.close()
