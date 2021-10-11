/**
 * @file   etch_a_sketch.c
 * @author Eliza Romeu
 * @date   10 October 2021
*/

#include <stdio.h>
#include <stdint.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <linux/i2c-dev.h>
#include <linux/i2c.h>
#include <sys/ioctl.h>

#include "smbus.c" 
#include "smbus.h" 
#include "adxl34x.c"
#include "adxl34x.h"


MODULE_LICENSE("GPL");
MODULE_AUTHOR("Eliza Romeu");
MODULE_DESCRIPTION("Etch a Sketch with Digital Accelerometer I2C Bus Driver");
MODULE_VERSION("0.1");

#define bus smbus.SMBus(1)
#define matrix 0x70
#define ADXL345	0xE5
#define sketch [0x00 for i in range(16)]
#define pen_position [1,2]

void i2c_Write_Byte(int fd, __u8 address, __u8 value)
{
   if (i2c_smbus_write_byte_data(fd, address, value) < 0) {
      close(fd);
      exit(1);
   }
}

void i2c_Read_Block(int fd, __u8 address, __u8 length, __u8 *values)
{
   if(i2c_smbus_read_i2c_block_data(fd, address,length,values)<0) {
      close(fd);
      exit(1);
   }
}

int i2c_Begin()
{
   int fd;
   char *fileName = "/dev/i2c-0";
   
   // Open port for reading and writing
   if ((fd = open(fileName, O_RDWR)) < 0)
      exit(1);
   
   // Set the port options and set the address of the device
   if (ioctl(fd, I2C_SLAVE, BMP085_I2C_ADDRESS) < 0) {               
      close(fd);
      exit(1);
   }

   return fd;
}

void matrix_Calibration()
{
	i2c_Begin();
	
	i2c_Write_Byte(fd,matrix,0x21);
	i2c_Write_Byte(fd,matrix,0x81);
	i2c_Write_Byte(fd,matrix,0x81);
}

int main(int argc, char **argv) {
	i2c_Begin();
	matrix_Calibration();
	
	sketch[2*pen_position[0]] = sketch[2*pen_position[0]] | (1<<(8-pen_position[1]));
	i2c_Write_Byte(fd, matrix, sketch);

	while(true){
		if (action == "up" and pen_position[1] < 8):
			pen_position = [pen_position[0], pen_position[1]+1];
		if (action == "down" and pen_position[1] > 1):
			pen_position = [pen_position[0], pen_position[1]-1];
		if (action == "left" and pen_position[0] < 8-1):
			pen_position = [pen_position[0]+1, pen_position[1]];
		if (action == "right" and pen_position[0] > 0):
			pen_position = [pen_position[0]-1, pen_position[1]];
		if (action == "shake"):
			sketch = [0x00 for i in range(16)];

		sketch[2*pen_position[0]]=sketch[2*pen_position[0]] | (1<<(8-pen_position[1]));
		i2c_Write_Byte(fd, matrix, sketch);
	}
			
	return 0;
}
