#!/usr/bin/python3 

import mysql.connector
import packageList
import serviceList
import sqlKeywords
import dumpsysChart
import checker
import datetime

def tableCreation():
    db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Password@123"
    )
    value = ""
    cursor = db.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS adbData;")

    cursor.execute("USE adbData")   
    now = datetime.datetime.now()
    s = now.strftime("%Y_%m_%d_%H_%M_%S")
    packageList.packageList()
    serviceList.serviceList()
    keywords = sqlKeywords.sqlKeywords()
    sql = "CREATE TABLE IF NOT EXISTS packageData_" +s+ " (Packages VARCHAR(255) NOT NULL, PRIMARY KEY(Packages));"
    cursor.execute(sql)
    sqle = "CREATE TABLE IF NOT EXISTS packageDumpsysData_"+s+" (Packages VARCHAR(255));"
    cursor.execute(sqle)
    
    with open("packageList.txt","r") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        sql = "INSERT INTO packageData_"+ s + " (Packages) VALUES (%s)"
        sqle = "INSERT INTO packageDumpsysData_"+s+ " (Packages) VALUES (%s)"
        for i in lines:
            value = i.replace("com.","")
            value = value.replace(".","_")
            cursor.execute(sql, (value,))
            db.commit()
            cursor.execute(sqle, (value,))
            db.commit()        
        f.close()

    with open("serviceList.txt","r") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        finalList_1 = []
        finalList_2 = []
        for i in lines:
            split_string = i.split(":",1)
            finalList_1.append(split_string[0])
        for i in finalList_1:
            finalList_2.append(i.replace(".","_"))
        for i in finalList_2:
            if i in keywords:
                i = i + "_"
                sql = "ALTER TABLE packageData_"+ s +" ADD COLUMN "+i+" INT;"  
                cursor.execute(sql)
                db.commit()
                sqle = "ALTER TABLE packageDumpsysData_"+s+" ADD COLUMN "+i+" MEDIUMTEXT;"  
                cursor.execute(sqle)               
                db.commit()
            else:
                sql = "ALTER TABLE packageData_"+s+" ADD COLUMN "+i+" INT;"  
                cursor.execute(sql)
                db.commit()
                sqle = "ALTER TABLE packageDumpsysData_"+s+" ADD COLUMN "+i+" MEDIUMTEXT;"  
                cursor.execute(sqle)
                db.commit()
    # print("ALTER TABLE packageData ADD COLUMN "+lines[0]+" INT;")
        f.close()
    print("Tables Created")
    dumpsysChart.dumpsysChart(keywords,s)

checker.checker()
tableCreation()