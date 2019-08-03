#!/usr/bin/python

"""
this script demonstrates how to create table in mysql database
"""

import pymysql

try :
  db = pymysql.connect('localhost','root','root','test_db')
except :
  print('can not connect to database')
  exit()

cursor = db.cursor()

cursor.execute('drop table if exists tb_employee')

sql_cmd = '''create table tb_employee (
	first_name char(20) not null,
	last_name char(20),
	age int,
	sex char(1),
	income float)'''

try:
    cursor.execute(sql_cmd)
except:
    print('can not create table employee')
    db.close()
    exit()

print('table employee is successfully created')
db.close()
