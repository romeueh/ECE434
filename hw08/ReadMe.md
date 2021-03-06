### Blinking an LED
hello.pru.c blinks an LED through the ARM GPIO structure.

To start run: bone$ make TARGET=hello.pru0 
To stop run:bone$ make TARGET=hello.pru0 stop
The fastest frequency I could get was 12.5MHz and the waveform has slight jitter, but for the most part it is stable. 

### PWM Generator
pwm1.pru0.c toggles an LED using the PRU.

The waveform is very stable and there was little to no jitter. I ran the waveform at 50MHz. 
I was unsure how record the standard deviation of the wave, but it should be a very small value.

*The 'scope can compute it*

### Controlling the PWM Frequency
pwm4.pru0.c will toggle 4 different channels.

The highest frequency I can is 630kHz. Overall the waveform was pretty stable with little jitter. 
I could change the count for each channel by altering the parameters of the four loop.

### Reading an Input at Regular Intervals
input.pru0.c reads an input pin and writes it to an output pin.

The I measure the transfer from input to the output to be 0.1 us.

### Analog Wave Generator
analog.pru0.c is used to output an analog signal using the GPIO pins. 

I followed the directions in the PRU cookbook and the signal strongly resembled a sinusoid.

### Overall Results
| File | Clock Speed |
| ----------- | ----------- |
|  hello.pru.c | 12.5MHz |
|  pwm1.pru0.c | 50 MHz |
|  pwm4.pru0.c | 630 kHz |

Images of different waveforms can be found in the Captures folder.

# hw08 grading

| Points      | Description |
| ----------- | ----------- |
| 14/14 | PRU
|  2/2 | Controlling the PWM Frequency - optional
|  2/2 | Reading an Input at Regular Intervals - optional
|  2/2 | Analog Wave Generator - optional
| 20/20 | **Total**

*Well done*

*My comments are in italics. --may*
