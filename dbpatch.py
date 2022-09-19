import sqlite3
import db_operations as db

import Admin_db_operations as adb




def patch1():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    a=db.peekcount1()
    a=a+1
    b="Table1"
    for row in cursor.execute("SELECT * from TABLE1"):
        c=row[0]
        d=row[1]
        e=row[3]

        adb.insert(a,b,c,d,e)
        
    conn.commit()
    conn.close()
    
def patch2():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    for row in cursor.execute("SELECT * from TABLE2"):
        a=row[0]
        b=row[1]
        c=row[2]
        d=row[3]

    conn.commit()
    conn.close()
    adb.insert(a,b,c,d)
def patch3():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    for row in cursor.execute("SELECT * from TABLE3"):
        a=row[0]
        b=row[1]
        c=row[2]
        d=row[3]

    conn.commit()
    conn.close()
    adb.insert(a,b,c,d)
def patch4():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    for row in cursor.execute("SELECT * from TABLE4"):
        a=row[0]
        b=row[1]
        c=row[2]
        d=row[3]

    conn.commit()
    conn.close()
    adb.insert(a,b,c,d)
def patch5():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    for row in cursor.execute("SELECT * from TABLE5"):
        a=row[0]
        b=row[1]
        c=row[2]
        d=row[3]

    conn.commit()
    conn.close()
    adb.insert(a,b,c,d)
def patch6():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    for row in cursor.execute("SELECT * from TABLE6"):
        a=row[0]
        b=row[1]
        c=row[2]
        d=row[3]

    conn.commit()
    conn.close()
    adb.insert(a,b,c,d)
def patch7():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    for row in cursor.execute("SELECT * from TABLE7"):
        a=row[0]
        b=row[1]
        c=row[2]
        d=row[3]

    conn.commit()
    conn.close()
    adb.insert(a,b,c,d)
def patch8():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    for row in cursor.execute("SELECT * from TABLE8"):
        a=row[0]
        b=row[1]
        c=row[2]
        d=row[3]

    conn.commit()
    conn.close()
    adb.insert(a,b,c,d)
def patch9():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    for row in cursor.execute("SELECT * from TABLE9"):
        a=row[0]
        b=row[1]
        c=row[2]
        d=row[3]

    conn.commit()
    conn.close()
    adb.insert(a,b,c,d)
def patch10():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    for row in cursor.execute("SELECT * from TABLE10"):
        a=row[0]
        b=row[1]
        c=row[2]
        d=row[3]

    conn.commit()
    conn.close()
    adb.insert(a,b,c,d)
 
patch1()
patch2()
patch3()
patch4()
patch5()
patch6()
patch7()
patch8()
patch9()
patch10() 
