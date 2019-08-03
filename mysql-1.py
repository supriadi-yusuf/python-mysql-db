#!/usr/bin/python

"""
this script demonstrates how make connection with mysql database
"""

import pymysql

try :
  # make connection
  # host : host, username : root, user password : root, database name = test_db
  db = pymysql.connect('localhost','root','root','test_db')
except :
  print('can not connect to database')
  exit()

cursor = db.cursor()
cursor.execute('select version()')
data = cursor.fetchone()

print('Database version : %s ' % data)

db.close()
