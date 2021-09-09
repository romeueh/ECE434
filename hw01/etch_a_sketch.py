#!/usr/bin/env python3
#chmod +x etch_a_sketch.py
#Author: Eliza Romeu

import time
import curses 
from curses import wrapper

max_height = 9
max_width = 9

def drawscreen(screen, sketch, pen_position):
    screen.clear()
    for i in range(9):
        for j in range(9):
            screen.addch(i*2, j*3, sketch[j][i])
    screen.refresh()
	

def clearscreen(screen):
    sketch = [[' ' for i in range(max_height)] for j in range(max_width)]
    screen.clear()
    screen.refresh()
    return sketch

def read_key(screen, pen_position):
	key_code = screen.getkey()
	if key_code == 'KEY_DOWN':
		if pen_position[1] > 0:
			pen_position = [pen_position[0], pen_position[1]-1]
	if key_code == 'KEY_UP':
		if pen_position[1] < max_height:
			pen_position = [pen_position[0], pen_position[1]+1]
	if key_code == 'KEY_RIGHT':
		if pen_position[0] < max_width:
			pen_position = [pen_position[0]+1, pen_position[1]]
	if key_code == 'KEY_LEFT':
		if pen_position[0] > 0:
			pen_position = [pen_position[0]-1, pen_position[1]]
	if key_code == ' ':
		clearscreen(screen)
	return pen_position;

def main(screen):
	screen.addstr("Welcome to the game Etch-A-Sketch! To begin use the arrow keys to direct the \npen on the screen. When you want to clear the screen press the space bar to \nshake the Etch-A-Sketch. Have fun!")
	screen.refresh()
	curses.napms(5000)
	
	sketch = clearscreen(screen)
	pen_position = [4,4]
	
	while(1):
		pen_position = read_key(screen, pen_position)
		sketch[pen_position[0]][pen_position[1]] = 'x'
		drawscreen(screen, sketch, pen_position)
		curses.napms(500)

screen = curses.initscr()
curses.wrapper(main)
