#2909 2025
#12:38
#parser for csv data into mysql db lokal

#husk at pathen er relativ til TERMINALEN og ikke filen her -- så hvis jeg
#står i "uge 3", så skal det være denne pathS

import csv
import sys

sys.path.insert(len(sys.path), 'mysql_stuff/')
from mysqltestcon import mycursor, cnx

def lookup_mfr(mfr):
    '''Look up the manufacturer's name from row[1],
    & return the proper name.'''
    if mfr == 'A':
        return 'American Home Food Products'
    if mfr == 'G':
        return 'General Mills' 
    if mfr ==  'K':
        return 'Kelloggs'
    if mfr == 'N':
        return 'Nabisco'
    if mfr == 'P':
        return 'Post'
    if mfr == 'Q':
        return 'Quaker Oats'
    if mfr == 'R':
        return 'Ralston Purina'

def create_mysql_insertion(row):
    '''Creates the SQL insertion string.'''
    mfr = lookup_mfr(row[1])
    row[1] = mfr
    sql2 = """INSERT INTO `corp_data`.`cereal_table` 
    (`name`, `mfr`, `type`, `calories`, `protein`, `fat`, `sodium`,
     `fiber`, `carbo`, `sugars`, `potassium`, `vitamins`, `shelf`, `weight`, `cups`, `rating`) 
     VALUES ("%s", '%s', '%s', '%d', '%d', '%d', '%d', '%f', '%f', '%d', '%d', '%d', '%d', '%f', '%f', '%f');""" % (row[0], row[1], row[2], int(row[3]), int(row[4]), int(row[5]), float(row[6]), float(row[7]), float(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), float(row[13]), float(row[14]), float(row[15]))
    #print("inside create_mysel_____________, sql2 string:", sql2)
    return sql2

'''This spamreader skips the first two rows in the csv file, 
& uses the create_mysql_insertion() method to create the mysql strings,
which it then commits.'''
with open('cereal_0001/data/cereal/Cereal.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    counter = 0
    for row in spamreader:
        #print(counter)
        if counter == 0:
            pass
            counter += 1
        elif counter == 1:
            counter += 1
            pass
        else:
            #print(' '.join(row))
            counter += 1
            #create sql statement
            sql = create_mysql_insertion(row)
            print("sql from parser:", sql)
            # print("val from parser:", val)
            # print("val from parser, type:", type(val))
            mycursor.execute(sql)
            cnx.commit()
