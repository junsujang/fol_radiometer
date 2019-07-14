#Jake Bernstein
import sys
sys.path.append("../pigpio")

import numpy as np

PIN_nOUTEN = 21
PIN_LATCHEN = 20
PIN_COUNTCLEAR = 16
PINS_LATCHDAT = [4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26]


def initCounterGPIO(pi):
    for pin in PINS_LATCHDAT:
        pi.set_mode(pin, pigpio.INPUT)
        pi.set_pull_up_down(pin, pigpio.PUD_OFF)
        
    for pin in [PIN_nOUTEN, PIN_LATCHEN]:
        pi.set_mode(pin, pigpio.OUTPUT)

    pi.write(PIN_nOUTEN,0)
    pi.write(PIN_LATCHEN,0)

def countPhotons(pi):
    print("Counting Photons")    
    pi.write(PIN_LATCHEN,1)
    pi.write(PIN_COUNTCLEAR,1)
    pi.write(PIN_COUNTCLEAR,0)
    rawdat = pi.read_bank_1()
    return orderbits(np.uint32(rawdat))

def orderbits(datin):
    datout = np.int32(0)
    for i in range(len(PINS_LATCHDAT)):
        bitdat = np.bitwise_and(1, np.right_shift(datin, PINS_LATCHDAT[i]))
        datout = datout + np.left_shift(bitdat,i)
        
