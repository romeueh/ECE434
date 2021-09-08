#!/usr/bin/env python3
#chmod +x etch_a_sketch.py
#Author: Eliza Romeu

import time
import curses 
from curses import wrapper

max_height = 8
max_width = 8

def drawscreen(screen):
	screen.refresh()

def read_key(screen, pen_position):
	key_code = screen.getch()
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
		screen.clear()
		screen.refresh()

def main(screen):
	screen.addstr("Welcome to the game Etch-A-Sketch! To begin use the arrow keys to direct the \npen on the screen. When you want to clear the screen press the space bar to \nshake the Etch-A-Sketch. Have fun!")
	screen.refresh()
	curses.napms(2000)
	screen.clear()
	pen_position = [0,0]
	while(1):
		read_key(screen, pen_position)
		drawscreen(screen)

screen = curses.initscr()
main(screen)
