#!/usr/bin/env python3
#chmod +x etch_a_sketch.py
#Author: Eliza Romeu

import time
import curses
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2
from curses import wrapper

global pen_position
global max_dim
global screen
global pos_changed

encoder1 = RotaryEncoder(eQEP1)
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

screen = curses.initscr()
screen.addstr("Welcome to the game Etch-A-Sketch! To begin use the four right-most buttons keys to direct the \npen on the screen. When you want to clear the screen press the 2nd button to \nshake the Etch-A-Sketch. Lastly, press the first button when you want to exit. Have fun!\n")
screen.addstr("\nWhat size would you like to board to be?")
screen.refresh()

max_dim = int(screen.getch())-47

def drawscreen(sketch):
	screen.clear()
	for i in range(max_dim):
		for j in range(max_dim):
			screen.addch(i*2, j*3, sketch[j][i])
	screen.refresh()

def clearscreen():
	screen.clear()
	sketch = [[' ' for i in range(max_dim)] for j in range(max_dim)]
	for i in range(max_dim):
		sketch[i][0] = chr(48 +i)
	for j in range(max_dim):
		sketch[0][j] = chr(48 +j)
	screen.refresh()
	return sketch

def main(screen):
	sketch = clearscreen()
	drawscreen(sketch)
	pen_position = [1,1]
	pos_changed = True
	rotary_vertical_position = encoder1.position
	rotary_horizontal_position = encoder2.position

	while(1):
		if (rotary_vertical_position > encoder1.position) and (pen_position[1] < max_dim-1):
			pen_position = [pen_position[0], pen_position[1]+1]
			rotary_vertical_position = encoder1.position
			pos_changed = True
		if (rotary_vertical_position < encoder1.position) and ( pen_position[1] > 1):
			pen_position = [pen_position[0], pen_position[1]-1]
			rotary_vertical_position = encoder1.position
			pos_changed = True
		if (rotary_horizontal_position > encoder2.position) and (pen_position[0] < max_dim-1):
			pen_position = [pen_position[0]+1, pen_position[1]]
			rotary_horizontal_position = encoder2.position
			pos_changed = True
		if (rotary_horizontal_position < encoder2.position) and (pen_position[0] > 1):
			pen_position = [pen_position[0]-1, pen_position[1]]
			rotary_horizontal_position = encoder2.position
			pos_changed = True
		if GPIO.event_detected(button_shake):
			sketch = clearscreen()
			pos_changed = True
		if GPIO.event_detected(button_exit):
			break
			
		if(pos_changed):
			sketch[pen_position[0]][pen_position[1]] = 'x'
			drawscreen(sketch)
			pos_changed = False
		curses.napms(10)

curses.wrapper(main)
