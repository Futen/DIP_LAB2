#! /usr/bin/env python

import subprocess
import glob

s = 'g++ -W  -O3 -I/usr/include/opencv lab2.cpp main.cpp -lm -lopencv_core -lopencv_highgui'
subprocess.call(s,shell=True)
