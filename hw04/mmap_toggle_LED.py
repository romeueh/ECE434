#!/usr/bin/env python3
# Credit: https://graycat.io/tutorials/beaglebone-io-using-python-mmap/
from mmap import mmap
import time, struct


GPIO1_startaddr = 0x4804c000
GPIO1_endaddr = 0x4804cfff
GPIO1_size = GPIO1_endaddr-GPIO1_startaddr
GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
USR3 = 1<<17

with open("/dev/mem", "r+b" ) as f:
  mem = mmap(f.fileno(), GPIO1_size, offset=GPIO1_startaddr)

packed_reg = mem[GPIO_OE:GPIO_OE+4]

reg_status = struct.unpack("<L", packed_reg)[0]

reg_status &= ~(USR3)

mem[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)

try:
  while(True):
    mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", USR3)

    mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", USR3)
 
except KeyboardInterrupt:
  mem.close()
