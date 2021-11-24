#!/usr/bin/python3 

import os
import re
import subprocess
import mysql.connector
import sqlKeywords
import checker
def dumpsysChart(keywords,time):
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
                checker.checker()
                args = "adb shell dumpsys " +j+ " " +i
                proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                output_1 = proc.stdout.read().decode()
                #print(output_1)
                if output_1 == "" or "Can't find service" in output_1:
                    s = j.replace(".","_")
                    d = i.replace("com.","")
                    d = d.replace(".","_")
                    if s in keywords:
                        s = s + "_"
                    sql = "UPDATE packageData_"+time+" SET "+s+"='0' WHERE Packages='"+d+"';"
                    cursor.execute(sql)
                    db.commit() 
                else:
                    s = j.replace(".","_")
                    d = i.replace("com.","")
                    d = d.replace(".","_")
                    if s in keywords:
                        s = s + "_"
                    sql = "UPDATE packageData_"+time+" SET "+s+"='1' WHERE Packages='"+d+"';"
                    cursor.execute(sql)
                    db.commit()
                    sqle = "UPDATE packageDumpsysData_"+time+" SET "+s+"= %s WHERE Packages= %s"
                    val = (output_1,d)
                    cursor.execute(sqle,val)
                    db.commit()
            print("Data inserted for "+i)