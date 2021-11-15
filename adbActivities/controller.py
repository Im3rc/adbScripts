#!/usr/bin/python3 

import mysql.connector
import packageList
import serviceList
import sqlKeywords
#import dumpsysChart
import checker
def tableCreation():
    db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Password@123"
    )

    cursor = db.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS adbData;")

    cursor.execute("USE adbData")   

    packageList.packageList()
    serviceList.serviceList()
    keywords = sqlKeywords.sqlKeywords()

    cursor.execute("CREATE TABLE IF NOT EXISTS packageData (Packages VARCHAR(255));")
    #cursor.execute("CREATE TABLE IF NOT EXISTS packageDumpsysData (Packages VARCHAR(255));")
    
    with open("packageList.txt","r") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        sql = """INSERT INTO packageData (Packages) VALUES (%s)"""
        #sqle = """INSERT INTO packageDumpsysData (Packages) VALUES (%s)"""
        for i in lines:
            value = i
            cursor.execute(sql, (value,))
            db.commit()
            #cursor.execute(sqle, (value,))
            #db.commit()            
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
                sql = "ALTER TABLE packageData ADD COLUMN "+i+" INT;"  
                cursor.execute(sql)
                db.commit()
                #sql = "ALTER TABLE packageDumpsysData ADD COLUMN "+i+" VARCHAR(255);"  
                #cursor.execute(sql)               
                #db.commit()
            else:
                sql = "ALTER TABLE packageData ADD COLUMN "+i+" INT;"  
                cursor.execute(sql)
                db.commit()
                #sql = "ALTER TABLE packageDumpsysData ADD COLUMN "+i+" VARCHAR(255);"  
                #cursor.execute(sql)
                #db.commit()
    # print("ALTER TABLE packageData ADD COLUMN "+lines[0]+" INT;")
        f.close()

    dumpsysChart.dumpsysChart(keywords)

checker.checker()
tableCreation()