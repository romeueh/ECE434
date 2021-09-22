#!/usr/bin/env python3
#chmod +x etch_a_sketch.py
#Author: Eliza Romeu

import time
import smbus
import curses
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP0, eQEP2
from curses import wrapper

global pen_position
global max_dim
global screen
global pos_changed

encoder1 = RotaryEncoder(eQEP0)
encoder2 = RotaryEncoder(eQEP2)

encoder1.setAbsolute()
encoder2.setAbsolute()
encoder1.enable()
encoder2.enable()

button_exit = "P9_13"
button_shake = "P9_14"

GPIO.setup(button_exit, GPIO.IN)
GPIO.setup(button_shake, GPIO.IN)
GPIO.add_event_detect(button_exit, GPIO.FALLING)
GPIO.add_event_detect(button_shake, GPIO.FALLING)

bus = smbus.SMBus(2)
matrix = 0x70

bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

screen = curses.initscr()
screen.addstr("Welcome to the game Etch-A-Sketch!\n")
screen.addstr("\nUse the two knobs to move the pen.")
screen.addstr("\nUse the right-most button to clear the screen.")
screen.addstr("\nUse the left-most button to exit.")
screen.refresh()

def drawscreen(sketch, pen_position):
	sketch[2*pen_position[0]]=sketch[2*pen_position[0]] | (1<<(8-pen_position[1]))
	bus.write_i2c_block_data(matrix, 0, sketch)

def clearscreen():
	sketch = [0x00 for i in range(16)]
	return sketch

def main(screen):
	sketch = clearscreen()
	pen_position = [1,1]
	drawscreen(sketch, pen_position)
	pos_changed = True
	rotary_vertical_position = encoder1.position
	rotary_horizontal_position = encoder2.position

	while(1):
		if (rotary_vertical_position > encoder1.position) and (pen_position[1] < 8):
			pen_position = [pen_position[0], pen_position[1]+1]
			rotary_vertical_position = encoder1.position
			pos_changed = True
		if (rotary_vertical_position < encoder1.position) and ( pen_position[1] > 1):
			pen_position = [pen_position[0], pen_position[1]-1]
			rotary_vertical_position = encoder1.position
			pos_changed = True
		if (rotary_horizontal_position < encoder2.position) and (pen_position[0] < 8-1):
			pen_position = [pen_position[0]+1, pen_position[1]]
			rotary_horizontal_position = encoder2.position
			pos_changed = True
		if (rotary_horizontal_position > encoder2.position) and (pen_position[0] > 0):
			pen_position = [pen_position[0]-1, pen_position[1]]
			rotary_horizontal_position = encoder2.position
			pos_changed = True
		if GPIO.event_detected(button_shake):
			sketch = clearscreen()
			pos_changed = True
		if GPIO.event_detected(button_exit):
			break
			
		if(pos_changed):
			screen.addstr("\n" + str(pen_position))
			screen.refresh()
			drawscreen(sketch, pen_position)
			pos_changed = False

curses.wrapper(main)
