#!/usr/bin/env python3
#chmod +x etch_a_sketch.py
#Author: Eliza Romeu

import time
import curses
import Adafruit_BBIO.GPIO as GPIO
from curses import wrapper

global clear
global exit
global pen_position
global max_dim
global screen
global sketch

clear = False
exit = False
pen_position = [1,1]
max_dim = 5

button_exit = "P9_13"
button_clear = "P9_14"
button_left = "P9_17"
button_right = "P9_18"
button_up = "P9_21"
button_down = "P9_22"

GPIO.setup(button_exit, GPIO.IN)
GPIO.setup(button_clear, GPIO.IN)
GPIO.setup(button_left, GPIO.IN)
GPIO.setup(button_right, GPIO.IN)
GPIO.setup(button_up, GPIO.IN)
GPIO.setup(button_down, GPIO.IN)

screen = curses.initscr()
screen.addstr("Welcome to the game Etch-A-Sketch! To begin use the arrow keys to direct the \npen on the screen. When you want to clear the screen press the space bar to \nshake the Etch-A-Sketch. Lastly, press q when you want to exit. Have fun!\n")
screen.addstr("\nWhat size would you like to board to be 1-9?")
screen.refresh()

max_dim = int(screen.getch())-47
sketch = [[' ' for i in range(max_dim)] for j in range(max_dim)];
for i in range(max_dim):
	sketch[i][0] = chr(48 +i)
for j in range(max_dim):
	sketch[0][j] = chr(48 +j)

def drawscreen():
	screen.clear()
	for i in range(max_dim):
		for j in range(max_dim):
			screen.addch(i*2, j*3, sketch[j][i])
	screen.refresh()

def clearscreen():
	sketch = [[' ' for i in range(max_dim)] for j in range(max_dim)]
	for i in range(max_dim):
		sketch[i][0] = chr(48 +i)
	for j in range(max_dim):
		sketch[0][j] = chr(48 +j)
	screen.clear()
	screen.refresh()

def read_button(channel):
	global pen_position
	global clear
	global exit
	if GPIO.input(channel) == 1:
		button_key = channel
		if (button_key == button_down) and (pen_position[1] < max_dim-1):
			pen_position = [pen_position[0], pen_position[1]+1]
		if (button_key == button_up) and ( pen_position[1] > 1):
			changed_pen_position = [pen_position[0], pen_position[1]-1]
		if (button_key == button_right) and (pen_position[0] < max_dim-1):
			changed_pen_position = [pen_position[0]+1, pen_position[1]]
		if (button_key == button_left) and (pen_position[0] > 1):
			changed_pen_position = [pen_position[0]-1, pen_position[1]]
		if button_key == button_clear:
			clear = True
		if button_key == button_exit:
			exit = True

GPIO.add_event_detect(button_exit, GPIO.FALLING, callback=read_button)
GPIO.add_event_detect(button_clear, GPIO.FALLING, callback=read_button)
GPIO.add_event_detect(button_left, GPIO.FALLING, callback=read_button)
GPIO.add_event_detect(button_right, GPIO.FALLING, callback=read_button)
GPIO.add_event_detect(button_up, GPIO.FALLING, callback=read_button)
GPIO.add_event_detect(button_down, GPIO.FALLING, callback=read_button)


def main(screen):
	drawscreen()

	while(1):
		drawscreen()
		if exit == True:
			break
		if clear == True:
			clearscreen(screen);
			clear = False
		sketch[pen_position[0]][pen_position[1]] = 'x'
		curses.napms(100)

curses.wrapper(main)
