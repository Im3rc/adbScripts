#!/usr/bin/python3 

import os
import subprocess
import packageList
import checker
import time
def monkeyRunner():
    k = 0
    checker.checker()
    packageList.packageList()
    with open("packageList_Monkey.txt") as f:
        k = k + 1
        packages = f.readlines()
        packages = [line.rstrip() for line in packages]
        for i in packages:
            args = "adb shell monkey -p "+i+" -v 1000" 
            proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            output_1 = proc.stdout.read().decode()
            processed_output = output_1.splitlines()
            print(str(k)+". "+i + "-- Finished")

monkeyRunner()




