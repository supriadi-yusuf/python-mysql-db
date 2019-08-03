#!/usr/bin/python

"""
this script demonstrates how to select record from table in mysql database and
fetch the result.
"""

import pymysql

try :
  db = pymysql.connect('localhost','root','root','test_db')
except :
  print('can not connect to database')
  exit()

cursor = db.cursor()

sql_cmd = "select * from tb_employee \
       where income >= %f" % \
       (1000)

try:
  cursor.execute(sql_cmd)
  n_employee = cursor.rowcount
  results = cursor.fetchall()

  print("there are %d employee" % n_employee)

  for row in results:
    fname = row[0]
    lname = row[1]
    age = row[2]
    sex = row[3]
    income = row[4]

    print("first name : %s, last name : %s, age = %d, sex = %c, income %.2f" % \
           ( fname, lname, age, sex, income))
except:
  print('unable to fetch data')
  db.close();raise

db.close()
