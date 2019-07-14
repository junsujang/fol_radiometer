#Jacob Bernstein
#Radiometer RPi GPIO test for photon counter and latch
#July 14, 2019

#Uses pigpio library, which needs daemon for python wrapper#Before running this function, call:
#'sudo pigpiod -s 1'
import sys
sys.path.append("../pigpio")
sys.path.append(".")
import numpy as np
import pigpio

import time

import radGPIO

pig = pigpio.pi()
radGPIO.initCounterGPIO(pig)
if len(sys.argv) == 1:
    nloops = 2
else:
    nloops = int(sys.argv[1])
    
#print('Hello World')
#print(str(nloops))
    
for i in range(nloops):
    numphotons = radGPIO.countPhotons(pig)
    print(str(numphotons))
    time.sleep(1)


