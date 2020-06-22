import RPi.GPIO as IO
from Libraries.constants import *
from Libraries.motion import *

pin_setup()

drive_forward_distance(3.24) #drive robot forward 3.24 meters