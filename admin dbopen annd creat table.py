import sqlite3

conn = sqlite3.connect('ADMIN.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE ADMIN
         (ID INTEGER PRIMARY KEY AUTOINCREMENT    NOT NULL,
         BILL          INT     NOT NULL,
         TABLE_NO         TEXT     NOT NULL,
         ITEM           TEXT    NOT NULL,
         QUANTITY        INT     NOT NULL,
         PRICE_TOTAL          INT     NOT NULL,
         DATE           TEXT    NOT NULL,
         TIME           TEXT    NOT NULL);''')
cursor.close()


