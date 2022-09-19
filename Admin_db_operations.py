import sqlite3
import time
from datetime import date

date=date.today().strftime('%d/%m/%Y')
time=time.strftime("%I:%M:%S %p")


def insert(a,b,c,d,e):
    global date
    global time
    conn = sqlite3.connect('ADMIN.sqlite')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO ADMIN (BILL,TABLE_NO ,ITEM,QUANTITY,PRICE_TOTAL,DATE,TIME) \
          VALUES (?,?,?,?,?,?,?)", (a,b,c,d,e,date,time));
    conn.commit()
    conn.close()



def peek():

    conn = sqlite3.connect('ADMIN.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT BILL from ADMIN"):
        
        cal=cal+row[5]

    conn.commit()
    conn.close()

    return cal




def del1():

    conn = sqlite3.connect('ADMIN.sqlite')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM ADMIN;',);
    cursor.execute('DELETE FROM sqlite_sequence;',)
        

    conn.commit()
    conn.close()


def peekbil():
    conn = sqlite3.connect('ADMIN.sqlite')
    cursor = conn.cursor()
    cal=0
    for row in cursor.execute("SELECT BILL from ADMIN"):
        cal=row[0]
    
    conn.commit()
    conn.close()
    return cal


