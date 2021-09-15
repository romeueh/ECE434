#!/usr/bin/env python3
#chmod +x etch_a_sketch.py
#Author: Eliza Romeu

import time
import curses
import Adafruit_BBIO.GPIO as GPIO
from curses import wrapper

global pen_position
global max_dim
global screen
global pos_changed

button_exit = "P9_13"
button_shake = "P9_14"
button_left = "P9_17"
button_right = "P9_18"
button_up = "P9_23"
button_down = "P9_24"

GPIO.setup(button_exit, GPIO.IN)
GPIO.setup(button_shake, GPIO.IN)
GPIO.setup(button_left, GPIO.IN)
GPIO.setup(button_right, GPIO.IN)
GPIO.setup(button_up, GPIO.IN)
GPIO.setup(button_down, GPIO.IN)

GPIO.add_event_detect(button_exit, GPIO.FALLING)
GPIO.add_event_detect(button_shake, GPIO.FALLING)
GPIO.add_event_detect(button_left, GPIO.FALLING)
GPIO.add_event_detect(button_right, GPIO.FALLING)
GPIO.add_event_detect(button_up, GPIO.FALLING)
GPIO.add_event_detect(button_down, GPIO.FALLING)

screen = curses.initscr()
screen.addstr("Welcome to the game Etch-A-Sketch! To begin use the arrow keys to direct the \npen on the screen. When you want to clear the screen press the space bar to \nshake the Etch-A-Sketch. Lastly, press q when you want to exit. Have fun!\n")
screen.addstr("\nWhat size would you like to board to be 1-9?")
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
	drawscreen()
	pen_position = [1,1]
	pos_changed = True

	while(1):
		if (GPIO.event_detected(button_down)) and (pen_position[1] < max_dim-1):
			pen_position = [pen_position[0], pen_position[1]+1]
			pos_changed = True
		if (GPIO.event_detected(button_up)) and ( pen_position[1] > 1):
			pen_position = [pen_position[0], pen_position[1]-1]
			pos_changed = True
		if (GPIO.event_detected(button_right)) and (pen_position[0] < max_dim-1):
			pen_position = [pen_position[0]+1, pen_position[1]]
			pos_changed = True
		if (GPIO.event_detected(button_left)) and (pen_position[0] > 1):
			pen_position = [pen_position[0]-1, pen_position[1]]
			pos_changed = True
		if GPIO.event_detected(button_shake):
			sketch = clearscreen()
			pos_changed = True
		if GPIO.event_detected(button_exit):
			break
			
		if(pos_changed):
			sketch[pen_position[0]][pen_position[1]] = 'x'
			drawscreen()
			pos_changed = False
		curses.napms(10)

curses.wrapper(main)
