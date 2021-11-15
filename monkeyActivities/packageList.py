#!/usr/bin/python3 

import os
import subprocess

def packageList():
    args = "adb shell pm list packages"
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    output_1 = proc.stdout.read().decode()
    processed_output = output_1.splitlines()
    finalList = {i.replace('package:','') for i in processed_output}
    packageFile = open("packageList.txt","w")
    for e in finalList:
        packageFile.write(e + "\n")
    packageFile.close()





