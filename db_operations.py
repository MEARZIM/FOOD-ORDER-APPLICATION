import sqlite3
conn = sqlite3.connect('TABLE_1.sqlite')
cursor = conn.cursor()



def insert1(a,b,c,d):

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO TABLE1 (ITEM,QUANTITY,PRICE,TOTAL) \
          VALUES (?,?,?,?)", (a,b,c,d));

    conn.commit()
    conn.close()
def peek1():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE1"):
        
        cal=cal+row[3]

    conn.commit()
    conn.close()

    return cal
def insert2(a,b,c,d):

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO TABLE2 (ITEM,QUANTITY,PRICE,TOTAL) \
          VALUES (?,?,?,?)", (a,b,c,d));

    conn.commit()
    conn.close()
def peek2():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE2"):
        
        cal=cal+row[3]

    conn.commit()
    conn.close()

    return cal
def insert3(a,b,c,d):

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO TABLE3 (ITEM,QUANTITY,PRICE,TOTAL) \
          VALUES (?,?,?,?)", (a,b,c,d));

    conn.commit()
    conn.close()
def peek3():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE3"):
        
        cal=cal+row[3]

    conn.commit()
    conn.close()

    return cal
def insert4(a,b,c,d):

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO TABLE4 (ITEM,QUANTITY,PRICE,TOTAL) \
          VALUES (?,?,?,?)", (a,b,c,d));

    conn.commit()
    conn.close()
def peek4():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE4"):
        
        cal=cal+row[3]

    conn.commit()
    conn.close()

    return cal
def insert5(a,b,c,d):

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO TABLE5 (ITEM,QUANTITY,PRICE,TOTAL) \
          VALUES (?,?,?,?)", (a,b,c,d));

    conn.commit()
    conn.close()
def peek5():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE5"):
        
        cal=cal+row[3]

    conn.commit()
    conn.close()

    return cal
def insert6(a,b,c,d):

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO TABLE6 (ITEM,QUANTITY,PRICE,TOTAL) \
          VALUES (?,?,?,?)", (a,b,c,d));

    conn.commit()
    conn.close()
def peek6():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE6"):
        
        cal=cal+row[3]

    conn.commit()
    conn.close()

    return cal
def insert7(a,b,c,d):

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO TABLE7 (ITEM,QUANTITY,PRICE,TOTAL) \
          VALUES (?,?,?,?)", (a,b,c,d));

    conn.commit()
    conn.close()
def peek7():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE7"):
        
        cal=cal+row[3]

    conn.commit()
    conn.close()

    return cal
def insert8(a,b,c,d):

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO TABLE8 (ITEM,QUANTITY,PRICE,TOTAL) \
          VALUES (?,?,?,?)", (a,b,c,d));

    conn.commit()
    conn.close()
def peek8():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE8"):
        
        cal=cal+row[3]

    conn.commit()
    conn.close()

    return cal
def insert9(a,b,c,d):

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO TABLE9 (ITEM,QUANTITY,PRICE,TOTAL) \
          VALUES (?,?,?,?)", (a,b,c,d));

    conn.commit()
    conn.close()
def peek9():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE9"):
        
        cal=cal+row[3]

    conn.commit()
    conn.close()

    return cal
def insert10(a,b,c,d):

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO TABLE10 (ITEM,QUANTITY,PRICE,TOTAL) \
          VALUES (?,?,?,?)", (a,b,c,d));

    conn.commit()
    conn.close()
def peek10():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE10"):
        
        cal=cal+row[3]

    conn.commit()
    conn.close()

    return cal
def del1():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM TABLE1;',);
        

    conn.commit()
    conn.close()
def del2():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM TABLE2;',);
        

    conn.commit()
    conn.close()
def del3():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM TABLE3;',);
        

    conn.commit()
    conn.close()
def del4():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM TABLE4;',);
        

    conn.commit()
    conn.close()
def del5():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM TABLE5;',);
        

    conn.commit()
    conn.close()
def del6():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM TABLE6;',);
        

    conn.commit()
    conn.close()
def del7():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM TABLE7;',);
        

    conn.commit()
    conn.close()
def del8():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM TABLE8;',);
        

    conn.commit()
    conn.close()
def del9():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM TABLE9;',);
        

    conn.commit()
    conn.close()
def del10():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM TABLE10;',);
        

    conn.commit()
    conn.close()
def peekcount1():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE1"):
        
        cal=cal+1

    conn.commit()
    conn.close()

    return cal
def peekcount2():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE2"):
        
        cal=cal+1

    conn.commit()
    conn.close()
def peekcount3():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE3"):
        
        cal=cal+1

    conn.commit()
    conn.close()

    return cal
def peekcount4():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE4"):
        
        cal=cal+1

    conn.commit()
    conn.close()
def peekcount5():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE5"):
        
        cal=cal+1

    conn.commit()
    conn.close()

    return cal
def peekcount6():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE6"):
        
        cal=cal+1

    conn.commit()
    conn.close()
def peekcount7():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE7"):
        
        cal=cal+1

    conn.commit()
    conn.close()

    return cal
def peekcount8():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE8"):
        
        cal=cal+1

    conn.commit()
    conn.close()
def peekcount9():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE9"):
        
        cal=cal+1

    conn.commit()
    conn.close()

    return cal
def peekcount10():

    conn = sqlite3.connect('TABLE_1.sqlite')
    cursor = conn.cursor()
    cal=0 
    for row in cursor.execute("SELECT ITEM,QUANTITY,PRICE,TOTAL from TABLE10"):
        
        cal=cal+1

    conn.commit()
    conn.close()
