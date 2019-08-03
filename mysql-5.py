#!/usr/bin/python

""""
this script demonstrates how to update data of a table in mysql database and
use transaction. 
"""

import pymysql

try :
  db = pymysql.connect('localhost','root','root','test_db')
except :
  print('can not connect to database')
  exit()

age = 40
sql_cmd = "update tb_employee set income = income + 0.1 * income \
where age >= %d" % (age)

cursor = db.cursor()

try:
  cursor.execute(sql_cmd)
  db.commit()
except:
  db.rollback()
  #raise

db.close()
