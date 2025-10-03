#2909 2025
#13:15
#skal have en database connection. bør teste det

import sys
sys.path.insert(len(sys.path), 'cereal_0001/data/__config')
from __config import Mysql
import mysql.connector


print("db_conn, starting ...")
cnx = mysql.connector.connect(user=Mysql.name, password=Mysql.pw, 
    host=Mysql.host, database=Mysql.schema)

cnx.cursor()
cnx.

cnx.close()
print("db_conn, ending ...")

#connect to db for test