#Jake Bernstein
import sys
sys.path.append("../pigpio")

import pigpio
import numpy as np
import time

PIN_nOUTEN = 21
PIN_LATCHEN = 20
PIN_COUNTCLEAR = 16
PIN_STROBE = 12
PIN_STATE = 18
PINS_LATCHDAT = [4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26]


def initCounterGPIO(pi):
    for pin in PINS_LATCHDAT + [PIN_STATE]:
        pi.set_mode(pin, pigpio.INPUT)
        pi.set_pull_up_down(pin, pigpio.PUD_OFF)
        
    for pin in [PIN_nOUTEN, PIN_LATCHEN, PIN_COUNTCLEAR, PIN_STROBE]:
        pi.set_mode(pin, pigpio.OUTPUT)

    pi.write(PIN_nOUTEN,0)
    pi.write(PIN_LATCHEN,1)
    pi.write(PIN_COUNTCLEAR,1)
    pi.write(PIN_COUNTCLEAR,0)
    pi.write(PIN_STROBE,0)
    return time.clock()

def countPhotons(pi):
    print("Counting Photons")
    #pi.write(PIN_STROBE,1)    
    pi.write(PIN_LATCHEN,0)
    pi.write(PIN_COUNTCLEAR,1)
    pi.write(PIN_COUNTCLEAR,0)
    rawdat = pi.read_bank_1()#notwe full bNK READ MAY INTRODUCE LATENCY ISSUES VIZ KERNEL BITCHYNESS
    #print(str(rawdat))
    pi.write(PIN_LATCHEN,1)
    #pi.write(PIN_STROBE,0)
    print('Hamamatsu state is {0}'.format(str(pi.read(PIN_STATE))))
    return orderbits(np.uint32(rawdat))

def orderbits(datin):
    datout = np.int32(0)
    for i in range(len(PINS_LATCHDAT)):
        bitmask = np.bitwise_and(datin,np.left_shift(1,PINS_LATCHDAT[i]))
        bitdat = np.bitwise_and(1, np.right_shift(bitmask, PINS_LATCHDAT[i]))
        datout = datout + np.left_shift(bitdat,i)
    return datout
        
def writencounts(pi,n):
    for i in range(n):
        pi.write(PIN_STROBE,1)
        pi.write(PIN_STROBE,0)