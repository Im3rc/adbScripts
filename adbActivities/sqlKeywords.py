#!/usr/bin/python3 

import mysql.connector


def sqlKeywords():
  db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "Password@123")
  cursor = db.cursor()

  cursor.execute("SELECT name FROM mysql.help_keyword;")

  result = cursor.fetchall()
  parsed_1 = []
  parsed_2 = []
  s = ''
  for i in result:
    s = ''.join(i)
    parsed_1.append(s.replace("('",""))
  for i in parsed_1:
    parsed_2.append(i.replace("',)",""))
  parsed_2.append("window")
  return(parsed_2)