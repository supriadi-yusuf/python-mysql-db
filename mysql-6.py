#!/usr/bin/python

""""
this script demonstrates how to delete data of a table in mysql database and
use transaction. 
"""

import pymysql

try :
  db = pymysql.connect('localhost','root','root','test_db')
except :
  print('can not connect to database')
  exit()

sql_cmd = "delete from tb_employee \
where income >= %d" % \
(1000)

cursor = db.cursor()

try:
  cursor.execute(sql_cmd)
  db.commit()

except ProgrammingError:
  db.rollback()
  print('Programming Error')

except DataError:
  db.rollback()
  print('Data Error')

except DatabaseError:
  db.rollback()
  print('Database Error')

except:
  db.rollback()
  print('Unknown Error')

finally:
  db.close()
  print('close connection')

print('data are deleted successfully')
