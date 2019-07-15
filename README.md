# fol_radiometer
Radiometer control code that runs on RPI at the moment

Steps for preparing a RPI to run this code:
(0) setup a wifi connection following:
	https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

(1) install openmp
	sudo apt-get install libomp-dev

(2) install wiringpi
	sudo apt-get install wiringpi

To compile:
gcc -Wall -fopenmp -lwiringPi -o radiometer radiometer.c -lrt 


for some reason, for wifi access, I also need to run
sudo wpa_cli -i wlan0 reconfigure 
upon log in...

pigpio is a separate github repo linked in our repo as a submodule. when cloning the repo, modify the call to get the submodule code:
'git clone --recursive [url]'
if you have a copy of the repo without the submodule code, call:
'git submodule update --init --recursive'
the pigpio code must be compiled. after pulling, cd into the pigpio folder and call make
in order to run pigpio with the python interface, first must start the daemon by calling:
sudo pigpiod
