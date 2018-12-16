# Simple_4x4_KeypadControllerForRaspberryPi
This project make the control of 4x4 keypad very easy. It is based on the original pad4pi keypad controller with slight adjustments.

# Wiring of the 4x4 keypad to the Raspberry Pi
Please refers to the following webpage to see how to connect the 4x4 keypad to your Raspberry Pi:
http://fahamni.tn/how-to-connect-and-use-4x4-keypad-using-raspberry-pi/

# Required libraries
Please refers to the following webpage  to see how to install the required libraries to well run the 4x4 keypad controller in your Raspberry Pi:
http://fahamni.tn/how-to-connect-and-use-4x4-keypad-using-raspberry-pi/

# How to use this controller?
In order to use this controller, you have to navigate to the keypad controller folder containing “keypadController.py” file and add the execution permission to this file using the following command:

    sudo chmod +x ./keypadController.py

Then, execute this file using the following command (in the same folder):

    ./keypadController.py

# Note: 
After finishing the modification of the behavior of various keys of the Keypad, you can add the following line to the crontab using the (crontab -e) command to launch the controller at the starting of the Raspberry Pi:

    @reboot /<here type the full path to the folder containing the folder of the controller>/keypadController.py

# What is the default behavior of this controller?
By pressing the keys on the keypad, the script prints the names of the various keys pressed in the terminal.

# Further tutorials
To explore other useful tutorials about Raspberry Pi and Android and web development, you can subsribe to our :
- Youtube Channel: https://www.youtube.com/channel/UCAXveSJOkPRjy77R6xT64kA
- Facebook Page: https://www.facebook.com/creative.team.tunisia/
- Our Websites newsLetter:  http://creativeteam.tn, http://fahamni.tn
