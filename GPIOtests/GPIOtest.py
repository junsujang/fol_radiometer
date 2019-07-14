#Jacob Bernstein
#Radiometer RPi GPIO test for photon counter and latch
#July 14, 2019

#Uses pigpio library, which needs daemon for python wrapper
#Before running this function, call:
#'sudo pigpiod -s 1'

import numpy as np
#import pigpio
import sys
import time

import radGPIO

#pig = pigpio.pi()
if len(sys.argv) == 0:
    nloops = 2
else:
    nloops = int(sys.argv[1])
    
#print('Hello World')
#print(str(nloops))
    
for i in range(nloops):
    radGPIO.countPhotons()
    time.sleep(1)


