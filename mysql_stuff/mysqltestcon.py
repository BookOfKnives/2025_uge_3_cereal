import mysql.connector
import sys

sys.path.insert(len(sys.path), 'cereal_0001/data/__config')
from __config import ConnectionInfo as cinf

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="horse drops to hell",
    database="corp_data"
)
cnx = mysql.connector.connect(
    user=cinf.user, 
    password=cinf.pw, 
    host=cinf.host, 
    database=cinf.database)
mycursor = cnx.cursor()


#mycursor = mydb.cursor()
#jeg mangler en IF NOT EXISTS create

# sql = "INSERT INTO test_table_01 (stuff, stuff) VALUES (%s, %s)"
# val = ("some vals", "some more vals")
# mycursor.execute(sql, val)
# mydb.commit()

#print(mycursor.rowcount, "mysql testcon, record inserted")



#jeg har denneher csv fil
#tag fil
#se på felter
#lav mysql inserts
