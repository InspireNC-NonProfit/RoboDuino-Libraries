'''
Use this file to declare constants to be used globally
Declare PINOUTS in this file
'''

import RPi.GPIO as IO

#----------- CONSTANT VALUES -----------------#

#Left Motor Pin GPIO Values
left_terma = 2
left_termb = 3

#Right Motor Pin GPIO Values
right_terma = 4
right_termb = 14

#Wheel Diameter in mm
wheel_diameter = 75


#----------- Methods --------------#
def pin_setup():
    print("Running Pin Setup...")

    IO.setwarnings(False)
    IO.setmode(IO.BCM)

    #Left Motors
    IO.setup(left_terma, IO.OUT)
    IO.setup(left_termb, IO.OUT)

    #Right Motors
    IO.setup(right_terma, IO.OUT)
    IO.setup(right_termb, IO.OUT)

    print("Pin Setup Complete")