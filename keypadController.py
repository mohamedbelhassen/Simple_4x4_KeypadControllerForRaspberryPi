#!/usr/bin/python
# -*- coding: latin-1 -*-

#this code is based on the code of the following URL: https://www.raspberrypi.org/learning/physical-computing-with-python/buzzer/
# keypad library:    https://pypi.org/project/pad4pi/1.0.0/

#Note: If you encounter the following error ( "/usr/bin/python^M : wrong interpreter, no file or directory of this type", you need to apply the following command dos2unix to the corresponding python file

from pad4pi import rpi_gpio
import time
import RPi.GPIO as GPIO


# in the following function, you can handle pressed keys------------------------------------------------------------------------------------------------------------------
def key_pressed(key):
	#in this demo library, we just print the pressed key in the terminal
	print(key)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------

minTimePeriodBetweenKeyPress=0.5 # in terms of seconds, you can slightly decrease this value to handle quicker press frequency, but this value is suitable for common use
KEYPAD = [
			["1","2","3","A"],
			["4","5","6","B"],
			["7","8","9","C"],
			["*","0","#","D"]
		]

GPIO.setmode(GPIO.BCM)       # set up BCM GPIO numbering  
#to get the BCM GPIO numbering used in the following two lines, open a terminal and execute the following command: "pinout"

COL_PINS = [13,6,5,0]		# set up BCM GPIO numbering
ROW_PINS = [21,20,26,19]  # BCM GPIO numbering
factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
keypad.registerKeyPressHandler(key_pressed)
print("Press on  Ctrl+C to exit this program")

try:
	while True:
		time.sleep(minTimePeriodBetweenKeyPress)

except KeyboardInterrupt:
    print("Keypad Controller is interrupted")
finally:
    keypad.cleanup()
