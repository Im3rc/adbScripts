#!/usr/bin/python3 

import os
import re
import subprocess
import mysql.connector
import sqlKeywords

def dumpsysChart(keywords):
    db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Password@123"
)

    cursor = db.cursor()
    cursor.execute("USE adbData")   

    with open("packageList.txt","r") as f1, open("serviceList.txt","r") as f2:
        packages = f1.readlines()
        packages = [line.rstrip() for line in packages]
        services = f2.readlines()
        services = [line.rstrip() for line in services]
        finalList_1 = []
        finalList_2 = []
        for i in services:
            split_string = i.split(":",1)
            finalList_1.append(split_string[0])      
        for i in packages:
            for j in finalList_1:
                args = "adb shell dumpsys " +j+ " " +i
                proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                output_1 = proc.stdout.read().decode()
                #print(output_1)
                if output_1 == "" or "Can't find service" in output_1:
                    s = j.replace(".","_")
                    if s in keywords:
                        s = s + "_"
                    sql = "INSERT INTO packageData ("+s+") VALUES (%s)"
                    val = ("0")
                    cursor.execute(sql,(val,))
                    db.commit()
                else:
                    s = j.replace(".","_")
                    if s in keywords:
                        s = s + "_"
                    sql = "INSERT INTO packageData ("+s+") VALUES (%s)"
                    val = ("1")
                    cursor.execute(sql,(val,))
                    db.commit()
                    #sql = "INSERT INTO packageDumpsysData ("+s+") VALUES (%s)"
                    #val = (output_1)
                    #cursor.execute(sql,(val,))
                    #db.commit()


keywords = sqlKeywords.sqlKeywords()
dumpsysChart(keywords)