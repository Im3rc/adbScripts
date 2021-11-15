#!/usr/bin/python3 

import os
import subprocess 
import sys
def checker():
    args = "adb devices"
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    output_1 = proc.stdout.read().decode()
    processed_output = output_1.splitlines()
    if len(processed_output) == 2:
    	print("ERROR - NO DEVICES CONNECTED")
    	sys.exit()
