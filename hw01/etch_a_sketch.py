#!/usr/bin/env python3
#chmod +x etch_a_sketch.py
#Author: Eliza Romeu

import time
import curses 
from curses import wrapper

max_height = 10
max_width = 10

def drawscreen(screen, sketch, pen_position):
    screen.clear()
    for i in range(max_height):
        for j in range(max_width):
            screen.addch(i*2, j*3, sketch[j][i])
    screen.refresh()
	

def clearscreen(screen):
    sketch = [[' ' for i in range(max_height)] for j in range(max_width)]
    for i in range(max_height):
    	sketch[i][0] = chr(48 +i)
    for j in range(max_width):
    	sketch[0][j] = chr(48 +j)
    screen.clear()
    screen.refresh()
    return sketch

def read_key(key_code, pen_position):
	if key_code == 'KEY_DOWN':
		if pen_position[1] < max_height-1:
			pen_position = [pen_position[0], pen_position[1]+1]
	if key_code == 'KEY_UP':
		if pen_position[1] > 1:
			pen_position = [pen_position[0], pen_position[1]-1]
	if key_code == 'KEY_RIGHT':
		if pen_position[0] < max_width-1:
			pen_position = [pen_position[0]+1, pen_position[1]]
	if key_code == 'KEY_LEFT':
		if pen_position[0] > 1:
			pen_position = [pen_position[0]-1, pen_position[1]]
	return pen_position;

def main(screen):
	screen.addstr("Welcome to the game Etch-A-Sketch! To begin use the arrow keys to direct the \npen on the screen. When you want to clear the screen press the space bar to \nshake the Etch-A-Sketch. Lastly, press q when you want to exit. Have fun!")
	screen.refresh()
	curses.napms(6000)
	
	sketch = clearscreen(screen)
	pen_position = [5,5]
	
	while(1):
		drawscreen(screen, sketch, pen_position)
		key_code = screen.getkey()
		pen_position = read_key(key_code, pen_position)
		if key_code == ' ':
			sketch = clearscreen(screen)
		if key_code == 'q':
			break
		sketch[pen_position[0]][pen_position[1]] = 'x'
		curses.napms(10)

screen = curses.initscr()
curses.wrapper(main)
