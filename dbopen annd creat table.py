import sqlite3

conn = sqlite3.connect('TABLE_1.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE TABLE1
         (ITEM           TEXT    NOT NULL,
         QUANTITY        INT     NOT NULL,
         PRICE          INT     NOT NULL,
         TOTAL          INT     NOT NULL);''')
cursor.close()

conn = sqlite3.connect('TABLE_1.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE TABLE2
         (ITEM           TEXT    NOT NULL,
         QUANTITY        INT     NOT NULL,
         PRICE          INT     NOT NULL,
         TOTAL          INT     NOT NULL);''')
cursor.close()

conn = sqlite3.connect('TABLE_1.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE TABLE3
         (ITEM           TEXT    NOT NULL,
         QUANTITY        INT     NOT NULL,
         PRICE          INT     NOT NULL,
         TOTAL          INT     NOT NULL);''')
cursor.close()

conn = sqlite3.connect('TABLE_1.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE TABLE4
         (ITEM           TEXT    NOT NULL,
         QUANTITY        INT     NOT NULL,
         PRICE          INT     NOT NULL,
         TOTAL          INT     NOT NULL);''')
cursor.close()

conn = sqlite3.connect('TABLE_1.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE TABLE5
         (ITEM           TEXT    NOT NULL,
         QUANTITY        INT     NOT NULL,
         PRICE          INT     NOT NULL,
         TOTAL          INT     NOT NULL);''')
cursor.close()

conn = sqlite3.connect('TABLE_1.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE TABLE6
         (ITEM           TEXT    NOT NULL,
         QUANTITY        INT     NOT NULL,
         PRICE          INT     NOT NULL,
         TOTAL          INT     NOT NULL);''')
cursor.close()

conn = sqlite3.connect('TABLE_1.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE TABLE7
         (ITEM           TEXT    NOT NULL,
         QUANTITY        INT     NOT NULL,
         PRICE          INT     NOT NULL,
         TOTAL          INT     NOT NULL);''')
cursor.close()

conn = sqlite3.connect('TABLE_1.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE TABLE8
         (ITEM           TEXT    NOT NULL,
         QUANTITY        INT     NOT NULL,
         PRICE          INT     NOT NULL,
         TOTAL          INT     NOT NULL);''')
cursor.close()

conn = sqlite3.connect('TABLE_1.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE TABLE9
         (ITEM           TEXT    NOT NULL,
         QUANTITY        INT     NOT NULL,
         PRICE          INT     NOT NULL,
         TOTAL          INT     NOT NULL);''')
cursor.close()

conn = sqlite3.connect('TABLE_1.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE TABLE10
         (ITEM           TEXT    NOT NULL,
         QUANTITY        INT     NOT NULL,
         PRICE          INT     NOT NULL,
         TOTAL          INT     NOT NULL);''')
cursor.close()

