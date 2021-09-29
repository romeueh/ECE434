#!/usr/bin/env python3
#chmod +x etch_a_sketch.py
#Author: Eliza Romeu

import time
import smbus
import numpy
import Adafruit_BBIO.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

bus = smbus.SMBus(1)
matrix = 0x70
sketch = [0x00 for i in range(16)]
pen_position = [1,2]

bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

sketch[2*pen_position[0]]=sketch[2*pen_position[0]] | (1<<(8-pen_position[1]))
bus.write_i2c_block_data(matrix, 0, sketch)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/<action>")
def action(action):
	global pen_position
	global sketch

	if (action == "up" and pen_position[1] < 8):
		pen_position = [pen_position[0], pen_position[1]+1]
	if (action == "down" and pen_position[1] > 1):
		pen_position = [pen_position[0], pen_position[1]-1]
	if (action == "left" and pen_position[0] < 8-1):
		pen_position = [pen_position[0]+1, pen_position[1]]
	if (action == "right" and pen_position[0] > 0):
		pen_position = [pen_position[0]-1, pen_position[1]]
	if (action == "shake"):
		sketch = [0x00 for i in range(16)]
			
	sketch[2*pen_position[0]]=sketch[2*pen_position[0]] | (1<<(8-pen_position[1]))
	bus.write_i2c_block_data(matrix, 0, sketch)
			
	return render_template('index.html')

if __name__ == "__main__":
        app.run(debug=True, port=8081, host='0.0.0.0')
