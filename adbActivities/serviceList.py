#!/usr/bin/python3 

import os
import re
import subprocess

def serviceList():
    args = "adb shell service list"
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    output_1 = proc.stdout.read().decode()
    processed_output = output_1.splitlines()
    del processed_output[0]
    #print(processed_output)
    finalList_1 = []
    finalList_2 = []
    procList = []
    reducedList = []
    for i in processed_output:
        procList.append(re.sub('^[0-9]*','',i))
    for i in procList:
        reducedList.append(i.replace("\t",""))
    serviceFile = open("serviceList.txt","w")
    for e in reducedList:
        serviceFile.write(e + "\n")
    serviceFile.close()

serviceList()


