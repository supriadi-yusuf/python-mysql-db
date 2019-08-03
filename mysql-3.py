#!/usr/bin/python

"""
this script demonstrates how to insert data into table in mysql database and
use transaction. rollback method is to cancel changes (insert/update/delete).
commit method is to save changes (insert/update/delete).
"""

import pymysql

try :
  db = pymysql.connect('localhost','root','root','test_db')
except :
  print('can not connect to database')
  exit()

cursor = db.cursor()

sql_cmd = '''insert into tb_employee (first_name, last_name, age, sex, income)
             values( 'supriadi', 'yusuf', 35, 'm', 1000)'''

sql_cmd2 = "insert into tb_employee \
            (first_name, last_name, age, sex, income) \
            values( '%s', '%s', %d, '%c', %f)" % \
            ( 'tsuni', 'wijaya', 45, 'm', 1500)

try:
  cursor.execute(sql_cmd)
  cursor.execute(sql_cmd2)
  db.commit()
except:
  print('can not insert data into table tb_employee')
  db.rollback()
  db.close(); raise #close db and show exception

print('data are successfully inserted')
db.close()
