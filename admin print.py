import sqlite3
import time
from datetime import date



def fetch():

    conn = sqlite3.connect('ADMIN.sqlite')
    cursor = conn.cursor()
    
    d="17/01/2022" 
    for row in cursor.execute("SELECT * from ADMIN where DATE = ?",(d,)):
        
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

    conn.commit()
    conn.close()







