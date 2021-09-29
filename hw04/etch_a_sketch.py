#!/usr/bin/env python3
#chmod +x etch_a_sketch.py
#Author: Eliza Romeu

import time
import smbus
import curses
import Adafruit_BBIO.GPIO as GPIO
from curses import wrapper
from flask import Flask, render_template, request
app = Flask(__name__)

global pen_position
global max_dim
global screen
global pos_changed

bus = smbus.SMBus(2)
matrix = 0x70

bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

screen = curses.initscr()
screen.addstr("Welcome to the game Etch-A-Sketch!\n")
screen.addstr("Open any web browser and browse to 192.168.7.2:8081")
screen.refresh()

def drawscreen(sketch, pen_position):
	sketch[2*pen_position[0]]=sketch[2*pen_position[0]] | (1<<(8-pen_position[1]))
	bus.write_i2c_block_data(matrix, 0, sketch)

def clearscreen():
	sketch = [0x00 for i in range(16)]
	return sketch

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	sketch = clearscreen()
	pen_position = [1,2]
	drawscreen(sketch, pen_position)
	pos_changed = True
	rotary_vertical_position = encoder1.position
	rotary_horizontal_position = encoder2.position

	while(1):
		if (action == "down"):
			if(pen_position[1] < 8):
				pen_position = [pen_position[0], pen_position[1]+1]
				pos_changed = True
			rotary_vertical_position = encoder1.position
		if (action == "up"):
			if(pen_position[1] > 1):
				pen_position = [pen_position[0], pen_position[1]-1]
				pos_changed = True
			rotary_vertical_position = encoder1.position
		if (action == "right"):
			if(pen_position[0] < 8-1):
				pen_position = [pen_position[0]+1, pen_position[1]]
				pos_changed = True
			rotary_horizontal_position = encoder2.position
		if (action == "left"):
			if(pen_position[0] > 0):
				pen_position = [pen_position[0]-1, pen_position[1]]
				pos_changed = True
			rotary_horizontal_position = encoder2.position
		if GPIO.event_detected(button_shake):
			sketch = clearscreen()
			pos_changed = True
		if GPIO.event_detected(button_exit):
			break
			
		if(pos_changed):
			drawscreen(sketch, pen_position)
			pos_changed = False
			
	return render_template('index.html', **templateData)

if __name__ == "__main__":
        app.run(debug=True, port=8081, host='0.0.0.0')
