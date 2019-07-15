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
starttime = radGPIO.initCounterGPIO(pig)
if len(sys.argv) == 1:
    nloops = 2
else:
    nloops = int(sys.argv[1])
    
#print('Hello World')
#print(str(nloops))
if 0:    
    totphotons = 0    
    for i in range(nloops):
        numphotons = radGPIO.countPhotons(pig)
        print(str(numphotons))
        #time.sleep(1)
        totphotons = totphotons + numphotons
    
    
    endtime = time.clock()
    elapsed = endtime-starttime
    print('Elapsed time: {0}\nTtotal photons: {1}\nFrequency: {2}'.format(str(elapsed),str(totphotons),str(totphotons/elapsed)))

if 0:
    logrange = np.logspace(0,3.5,nloops)
    logrange = logrange.astype(int)
    numpassed = 0
    print('Testing the following count numbers:')
    print(*logrange)
    for i in logrange:
        radGPIO.writencounts(pig,i)
        numcounted = radGPIO.countPhotons(pig)
        if numcounted==i:
            numpassed = numpassed + 1
        else:
            print('Wrote {0} counts, Read {1} counts'.format(i,numcounted))

    print('Passed {0} out of {1} tests'.format(numpassed,nloops))
    
if 1:
    while 1:
        numphotons = radGPIO.countPhotons(pig)
        print('Counted {0} photons'.format(numphotons))
        
