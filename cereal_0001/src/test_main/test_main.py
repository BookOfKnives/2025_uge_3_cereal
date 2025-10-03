#0110 2025
#13:46
#main class?

import sys
sys.path.insert(len(sys.path), 'cereal_0001/data/__config')
from __config import ConnectionInfo as cinf

#0110 2025 14:36
#det her ku godt være i sin egen modul
import mysql.connector
cnx = mysql.connector.connect(
    user=cinf.user, 
    password=cinf.pw, 
    host=cinf.host, 
    database=cinf.schema)
mycursor = cnx.cursor()

#0110 2025 14:30
#det her virker
print("trying to insert")
sql = "INSERT INTO test_table_01 (first_column) VALUES (%s)"
val = (444,)
mycursor.execute(sql, val)
cnx.commit()

print("Done!")
#test connection til db

#tøm schema
#opret schema

#csv parser; tag csv fil, og skab
#sql vlues ud fra den 

